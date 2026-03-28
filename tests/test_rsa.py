# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilo
import utilosafe.public
import utilosafe.rsa
import utilotest

import utilosafe


@utilotest.longrun
def test_generate_write_load_rsa(testdir):
    outfile = testdir.tmpdir.join('rsa')
    private = utilosafe.create_private_key()
    expected = utilosafe.create_public_key(private)
    # write file
    utilosafe.write_rsa(outfile, expected)
    # create RSA object
    loaded = utilosafe.rsa.dump_public_key(utilosafe.load_rsa_public(outfile))
    assert loaded == expected


@pytest.mark.xfail(reason='rework large encryption')
@utilotest.nightly
def test_write_large_file(testdir):
    loaded = utilo.file_read_binary(power.BACHELOR128_PDF)
    private = utilosafe.create_private_key()
    public = utilosafe.create_public_key(private)
    # write file
    encrypted = utilosafe.encrypt(loaded, public)
    utilo.file_create('blabla', encrypted)
    decrypted = utilosafe.decrypt(encrypted, private)
    assert len(decrypted) == len(loaded)
    assert decrypted == loaded


def test_public_special_bytes():
    """Do not remove starting \x00-zero bits when using rsa decryption."""
    data = (b'\x00\x00\x00\x00\xf4\x0b;\xc77\xdd\xe5\x97\x08'
            b'\xdd2\x12\x9f#\xe0\x98\xd0I\xedv\xd3-\xa6\xa6')
    private = utilosafe.create_private_key()
    public = utilosafe.create_public_key(private)
    encrypted = utilosafe.encrypt(data, public)
    decrypted = utilosafe.decrypt(encrypted, private)
    assert decrypted == data


def test_public_password(testdir, monkeypatch):
    data = b'Helm is Hier'
    private = utilosafe.create_private_key()
    public = utilosafe.create_public_key(private)
    utilosafe.write_rsa('public.pem', public)
    path = str(testdir.tmpdir.join('public.pem'))
    with monkeypatch.context() as context:
        utilosafe.public_password.cache_clear()
        context.setenv(utilosafe.UTILOSAFE_PUBLIC_KEY, path)
        encrypted = utilosafe.encrypt(data)
        assert encrypted != data
    decrypted = utilosafe.decrypt(encrypted, key=private)
    assert decrypted == data
