# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilosafe


def test_encrypt_large_data():
    loaded = os.urandom(1024 * 1024 * 120)  # 120 MB
    encrypted = utilosafe.encrypt(loaded)
    assert encrypted != loaded
    decrypted = utilosafe.decrypt(encrypted)
    assert len(decrypted) == len(loaded)
    assert decrypted == loaded
