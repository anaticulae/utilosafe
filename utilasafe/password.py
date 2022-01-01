# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
from Crypto.Cipher import AES

import utilasafe
import utilasafe.utils


def encrypt(plaintext: bytes) -> bytes:
    r"""Convert plain text to cipher text.

    >>> encrypt(b'hello')
    b'V\xcdj\xdf\xbf\x03\xb1\xf6\xb33JH\xc9\x8eO?1\x15ye\x94b\xc6:\xad\xb18\xdeL\x93\x86\x83'
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
    result = AES.new(pwd, AES.MODE_ECB)
    return result
