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

BLOCKSIZE = 32


def encrypt(data: bytes, public: bytes = None) -> int:
    if public is None:
        rsa = utilasafe.public_password()
    else:
        rsa = utilasafe.rsa.create_rsa(public)

    encrypted = [
        str(rsa._encrypt(bytes_to_long(block))) for block in split(data)  # pylint:disable=W0212
    ]
    result = '\n'.join(encrypted)
    return result


def decrypt(data: bytes, private: bytes = None) -> bytes:
    rsa = utilasafe.rsa.create_rsa(private)
    decrypted = [
        long_to_bytes(rsa._decrypt(int(block))) for block in data.splitlines()  # pylint:disable=W0212
    ]
    # remove magic start bit
    nomagic = [item[1:] for item in decrypted]
    result = b''.join(nomagic)
    return result


def split(data, length=BLOCKSIZE):
    # TODO: REPLACE WITH PYTHONIC ONE
    start = 0
    while data[start:start + length]:
        # add magic start bit to avoid cutting \x00 when converting to long
        yield b'\x01' + data[start:start + length]
        start += BLOCKSIZE
