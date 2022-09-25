# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utila
import utilatest

import utilasafe
import utilasafe.public
import utilasafe.rsa


@utilatest.longrun
def test_generate_write_load_rsa(testdir):
    outfile = testdir.tmpdir.join('rsa')
    private = utilasafe.create_private_key()
    expected = utilasafe.create_public_key(private)
    # write file
    utilasafe.write_rsa(outfile, expected)
    # create RSA object
    loaded = utilasafe.rsa.dump_public_key(utilasafe.load_rsa_public(outfile))
    assert loaded == expected


@pytest.mark.xfail(reason='rework large encryption')
@utilatest.nightly
def test_write_large_file(testdir):
    loaded = utila.file_read_binary(power.BACHELOR128_PDF)
    private = utilasafe.create_private_key()
    public = utilasafe.create_public_key(private)
    # write file
    encrypted = utilasafe.encrypt(loaded, public)
    utila.file_create('blabla', encrypted)
    decrypted = utilasafe.decrypt(encrypted, private)
    assert len(decrypted) == len(loaded)
    assert decrypted == loaded


def test_public_special_bytes():
    """Do not remove starting \x00-zero bits when using rsa decryption."""
    data = (b'\x00\x00\x00\x00\xf4\x0b;\xc77\xdd\xe5\x97\x08'
            b'\xdd2\x12\x9f#\xe0\x98\xd0I\xedv\xd3-\xa6\xa6')
    private = utilasafe.create_private_key()
    public = utilasafe.create_public_key(private)
    encrypted = utilasafe.encrypt(data, public)
    decrypted = utilasafe.decrypt(encrypted, private)
    assert decrypted == data


def test_public_password(testdir, monkeypatch):
    data = b'Helm is Hier'
    private = utilasafe.create_private_key()
    public = utilasafe.create_public_key(private)
    utilasafe.write_rsa('public.pem', public)
    path = str(testdir.tmpdir.join('public.pem'))
    with monkeypatch.context() as context:
        utilasafe.public_password.cache_clear()
        context.setenv(utilasafe.UTILASAFE_PUBLIC_KEY, path)
        encrypted = utilasafe.encrypt(data)
        assert encrypted != data
    decrypted = utilasafe.decrypt(encrypted, key=private)
    assert decrypted == data
