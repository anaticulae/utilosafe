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
import utilatest

import utilasafe


@utilatest.longrun
def test_generate_write_load_rsa(testdir):
    outfile = os.path.join(testdir.tmpdir, 'rsa')
    public = utilasafe.rsa.create_private_key()
    expected = utilasafe.rsa.create_rsa(public)
    # write file
    utilasafe.write_rsa(outfile, public)
    # create RSA object
    loaded = utilasafe.load_rsa(outfile)
    assert loaded == expected


def test_public_password(testdir, monkeypatch):
    data = b'Helm is Hier'
    private = utilasafe.create_private_key()
    public = utilasafe.create_public_key(private)
    utilasafe.write_rsa('public.pem', public)
    path = str(os.path.join(testdir.tmpdir, 'public.pem'))
    with monkeypatch.context() as context:
        context.setenv('UTILASAFE_PUBLIC_KEY', path)
        encrypted = utilasafe.encrypt_public(data)
        assert encrypted != data
    decrypted = utilasafe.decrypt_public(encrypted, private)
    assert decrypted == data
