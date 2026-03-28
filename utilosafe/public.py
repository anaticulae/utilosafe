# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
>>> import utilosafe.rsa

>>> PRIVATE = utilosafe.rsa.create_private_key()
>>> PUBLIC = utilosafe.rsa.create_public_key(PRIVATE)

>>> encrypted = encrypt(b'Hello', public=PUBLIC)
>>> decrypt(encrypted, PRIVATE)
b'Hello'
"""

import utilosafe.rsa
import utilosafe.utils


def encrypt(plaintext: bytes, public: bytes = None) -> int:
    if public is None:
        public = utilosafe.utils.public_password()
    result = utilosafe.rsa.encrypt(
        plaintext,
        public,
    )
    return result


def decrypt(ciphertext: bytes, key: str, passphrase: bytes = None) -> bytes:
    result = utilosafe.rsa.decrypt(
        ciphertext,
        key,
        passphrase=passphrase,
    )
    return result
