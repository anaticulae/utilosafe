# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools
import os

import utilo
import utilosafe.cli
import utilotest

import utilosafe

run = functools.partial(
    utilotest.run_cov,
    process='safeme_create',
    main=utilosafe.cli.main,
    expect=True,
)


@utilotest.longrun
def test_generate_cli(testdir, monkeypatch):
    password = b'helm'
    utilo.file_create_binary('password', password)
    with monkeypatch.context() as context:
        context.setattr(
            utilosafe.cli,
            'insert_password',
            lambda: password,
        )
        # safeme_create < password
        run('', mp=monkeypatch)
    private = str(testdir.tmpdir.join('private.pem'))
    loaded = utilosafe.load_rsa_private(  # nosec
        private,
        passphrase=b'helm',
    )
    assert loaded
    assert os.path.exists('private.pem')
    assert os.path.exists('public.pem')
