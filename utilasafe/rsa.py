# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> import utilasafe.rsa

>>> PRIVATE = utilasafe.rsa.create_private_key()
>>> PUBLIC = utilasafe.rsa.create_public_key(PRIVATE)

>>> encrypted = encrypt(b'Hello', public=PUBLIC)
>>> decrypt(encrypted, PRIVATE)
b'Hello'
"""

import utila
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

PUBLIC_EXPONENT = 65537

PADDING = padding.PKCS1v15()


def encrypt(plaintext: bytes, public: bytes) -> int:
    if isinstance(public, bytes):
        public = serialization.load_ssh_public_key(public)
    result = public.encrypt(
        plaintext=plaintext,
        padding=PADDING,
    )
    return result


def decrypt(ciphertext: bytes, path: str, passphrase: bytes = None) -> bytes:
    loaded = load_rsa_private(path, passphrase=passphrase)
    result = loaded.decrypt(
        ciphertext=ciphertext,
        padding=PADDING,
    )
    return result


def create_private_key(passphrase: bytes = None, bits: int = 1024) -> bytes:
    r"""\
    >>> create_private_key(b'HelmIsSafe')
    b'-----BEGIN OPENSSH PRIVATE KEY-----...---END OPENSSH PRIVATE KEY-----\n'
    """
    private = rsa.generate_private_key(
        public_exponent=PUBLIC_EXPONENT,
        key_size=bits,
    )
    algo = serialization.NoEncryption()
    if passphrase:
        algo = serialization.BestAvailableEncryption(password=passphrase)  # pylint:disable=R0204
    result = private.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=algo,
    )
    return result


def create_public_key(private: bytes, passphrase=None) -> bytes:
    """\
    >>> create_public_key(create_private_key())
    b'ssh-rsa ...=='
    >>> create_public_key(create_private_key(passphrase=b'helm'), b'helm')
    b'ssh-rsa ...=='
    """
    result = serialization.load_ssh_private_key(
        data=private,
        password=passphrase,
    )
    public = result.public_key()
    result = dump_public_key(public)
    return result


def dump_public_key(public) -> bytes:
    result = public.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH,
    )
    return result


def write_rsa(path, key: bytes):
    utila.file_replace_binary(path, key)


def load_rsa_private(
    path,
    passphrase: bytes = None,
) -> '_SSH_PRIVATE_KEY_TYPES':
    if isinstance(path, str):
        loaded = utila.file_read_binary(path)
    else:
        loaded = path
    result = serialization.load_ssh_private_key(
        data=loaded,
        password=passphrase,
    )
    return result


def load_rsa_public(path) -> '_SSH_PUBLIC_KEY_TYPES':
    data = utila.file_read_binary(path)
    result = serialization.load_ssh_public_key(data=data)
    return result
