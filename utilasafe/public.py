# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
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

from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

import utilasafe
import utilasafe.rsa


def encrypt(data: bytes, public: bytes = None) -> int:
    if public is None:
        rsa = utilasafe.public_password()
    else:
        rsa = utilasafe.rsa.create_rsa(public)
    data = bytes_to_long(data)
    result = rsa._encrypt(data) # pylint:disable=W0212
    return result


def decrypt(data: bytes, private: bytes = None) -> bytes:
    rsa = utilasafe.rsa.create_rsa(private)
    decrypted = rsa._decrypt(data) # pylint:disable=W0212
    result = long_to_bytes(decrypted)
    return result
