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

import cryptography.hazmat.primitives.asymmetric.padding as padding
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
import cryptography.hazmat.primitives.serialization as serialization
import utila

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
    password = getpassword(passphrase=passphrase)
    result = private.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=password,
    )
    return result


def create_public_key(private: bytes, passphrase=None) -> bytes:
    """\
    >>> create_public_key(create_private_key())
    b'ssh-rsa ...=='
    """
    if passphrase:
        passphrase = getpassword(passphrase)
    result = serialization.load_ssh_private_key(
        data=private,
        password=passphrase,
    )
    public = result.public_key()
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
    if passphrase:
        passphrase = getpassword(passphrase)
    result = serialization.load_ssh_private_key(
        data=loaded,
        password=passphrase,
    )
    return result


def load_rsa_public(path) -> '_SSH_PUBLIC_KEY_TYPES':
    data = utila.file_read_binary(path)
    result = serialization.load_ssh_public_key(data=data)
    return result


def getpassword(passphrase: bytes = None):
    if not passphrase:
        return serialization.NoEncryption()
    assert isinstance(passphrase, bytes)
    result = serialization.BestAvailableEncryption(password=passphrase)
    return result
