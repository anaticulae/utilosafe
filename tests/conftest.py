# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilo

import utilosafe

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name


@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    password = utilo.tmpname(width=32)
    monkeypatch.setenv(
        utilosafe.UTILOSAFE_USER_PASSWORD,
        password,
    )
