# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import utilasafe
import utilasafe.utils


def encrypt(plaintext: bytes) -> bytes:
    r"""Convert plain text to cipher text.

    >>> len(encrypt(b'hello')) > 25
    True
    >>> decrypt(encrypt(b'hello'))
    b'hello'
    """
    if isinstance(plaintext, str):
        plaintext = plaintext.encode(
            encoding='utf8',
            errors='xmlcharrefreplace',
        )
    plaintext = utilasafe.utils.create_block(plaintext)
    ciphertext = aes().encrypt(plaintext)
    return ciphertext


def decrypt(ciphertext: bytes, string: bool = False) -> bytes:
    """Convert cipher text to plain text."""
    plaintext = aes().decrypt(ciphertext)
    plaintext = utilasafe.utils.remove_block(plaintext)
    if string:
        plaintext: str = plaintext.decode(encoding='utf8')
    return plaintext


def aes():
    pwd = utilasafe.user_password()
    # normalize password
    pwd = utila.secure_hash(pwd, digits=32)
    pwd: bytes = pwd.encode('utf8')
    # TODO: VERIFY PROS AND CONS OF MODE
    try:
        from Crypto.Cipher import AES  # nosec # TODO: VERIFY THIS
    except ImportError:
        utila.error('could not import Crypto.Cipher')
        return NoPassword()
    result = AES.new(pwd, AES.MODE_ECB)
    return result


class NoPassword:

    def decrypt(self, ciphertext):  # pylint:disable=R0201
        return ciphertext

    def encrypt(self, plaintext):  # pylint:disable=R0201
        return plaintext
