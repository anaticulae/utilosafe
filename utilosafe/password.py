# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

import utilosafe
import utilosafe.utils


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
    nonce = os.urandom(12)
    key, salt = aes()
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)
    # Format: salt (16) + nonce (12) + ciphertext + tag (16)
    return salt + nonce + ciphertext


def decrypt(ciphertext: bytes) -> bytes:
    """Convert cipher text to plain text."""

    salt = ciphertext[:16]
    nonce = ciphertext[16:28]
    ciphertext = ciphertext[28:]

    key = derive_key(load_password(), salt)

    plaintext = AESGCM(key).decrypt(
        nonce,
        ciphertext,
        None,
    )
    return plaintext


def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,  # AES-256
        n=2**15,
        r=8,
        p=1)
    return kdf.derive(password)


def load_password():
    pwd = utilosafe.user_password()
    # normalize password
    pwd = utilo.secure_hash(pwd, digits=32)
    pwd: bytes = pwd.encode('utf8')
    return pwd


def aes():
    salt = os.urandom(16)
    pwd = load_password()
    result = derive_key(pwd, salt), salt
    return result


class NoPassword:

    def decrypt(self, ciphertext):  # pylint:disable=R0201
        return ciphertext

    def encrypt(self, plaintext):  # pylint:disable=R0201
        return plaintext
