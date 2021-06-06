# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

from Crypto.PublicKey import RSA


def create_private_key() -> bytes:
    rsa = RSA.generate(3072)
    result = rsa.export_key()
    return result


def create_public_key(private: bytes) -> bytes:
    """\
    >>> create_public_key(create_private_key())
    b'-----BEGIN PUBLIC KEY...-----END PUBLIC KEY-----'
    """
    public = create_rsa(private)
    result = public.publickey().export_key()
    return result


def create_rsa(key: bytes) -> RSA:
    """\
    >>> create_rsa(create_public_key(create_private_key()))
    RsaKey(n=...)
    """
    rsa = RSA.import_key(key)
    return rsa
