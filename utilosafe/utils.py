# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import math

import configo
import utilo

import utilosafe

BLOCKSIZE = 32

UTILOSAFE_PUBLIC_KEY = 'UTILOSAFE_PUBLIC_KEY'  # nosec
UTILOSAFE_USER_PASSWORD = 'UTILOSAFE_USER_PASSWORD'  # nosec


def create_block(content: bytes, blocksize: int = BLOCKSIZE) -> bytes:
    """\
    >>> create_block(b'abc' * 15)
    b'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabc                   '
    """
    if not len(content) % blocksize:
        return content
    missing = math.ceil(len(content) / blocksize) * blocksize - len(content)
    content = content + b' ' * missing
    return content


def remove_block(content: bytes) -> bytes:
    stripped = content.rstrip()
    if content[len(stripped):len(stripped) + 1] == b'\n':
        # valid file ends with newline
        stripped = content[0:len(stripped) + 1]
    return stripped


@utilo.cacheme
def user_password() -> str:
    result = configo.env(UTILOSAFE_USER_PASSWORD, 'NOPASSWORD')
    return result


@utilo.cacheme
def public_password() -> 'RSA':
    path = configo.env(UTILOSAFE_PUBLIC_KEY, None)
    if not path:
        utilo.error(f'missing env {UTILOSAFE_PUBLIC_KEY}')
        return None
    result = utilosafe.load_rsa_public(path)
    return result
