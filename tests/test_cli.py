# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import utilasafe


def test_generate_cli(testdir):
    utila.file_create('password', 'helm')
    utila.run('safeme_create < password')
    private = os.path.join(testdir.tmpdir, 'private.pem')
    loaded = utilasafe.load_rsa(private, passphrase='helm')
    assert loaded
    assert os.path.exists('private.pem')
    assert os.path.exists('public.pem')
