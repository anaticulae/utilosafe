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

import utilasafe.rsa
import utilasafe.utils


def encrypt(plaintext: bytes, public: bytes = None) -> int:
    if public is None:
        public = utilasafe.utils.public_password()
    result = utilasafe.rsa.encrypt(
        plaintext,
        public,
    )
    return result


def decrypt(ciphertext: bytes, key: str, passphrase: bytes = None) -> bytes:
    result = utilasafe.rsa.decrypt(
        ciphertext,
        key,
        passphrase=passphrase,
    )
    return result
