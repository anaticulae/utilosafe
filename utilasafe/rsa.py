# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
from Crypto.PublicKey import DSA  # pylint:disable=W0611
from Crypto.PublicKey import RSA


def create_private_key(passphrase=None, bits: int = 1024) -> bytes:
    """\
    >>> create_private_key('HelmIsSafe')
    b'...Proc-Type: 4,ENCRYPTED...'
    """
    rsa = RSA.generate(bits=bits)
    result = rsa.export_key(passphrase=passphrase)
    return result


def create_public_key(private: bytes, passphrase=None) -> bytes:
    """\
    >>> create_public_key(create_private_key())
    b'-----BEGIN PUBLIC KEY...-----END PUBLIC KEY-----'
    """
    public = create_rsa(private, passphrase=passphrase)
    result = public.publickey().export_key()
    return result


def create_rsa(key: bytes, passphrase=None) -> RSA:
    """\
    >>> create_rsa(create_public_key(create_private_key()))
    RsaKey(n=...)
    """
    rsa = RSA.import_key(key, passphrase=passphrase)
    return rsa


def write_rsa(path, key: bytes):
    utila.file_replace_binary(path, key)


def load_rsa(path, passphrase=None) -> RSA:
    loaded = utila.file_read_binary(path)
    result = create_rsa(loaded, passphrase=passphrase)
    return result
