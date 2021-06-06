# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilasafe.rsa


def test_generate_write_load_rsa(testdir):
    outfile = os.path.join(testdir.tmpdir, 'rsa')
    public = utilasafe.rsa.create_private_key()
    expected = utilasafe.rsa.create_rsa(public)
    # write file
    utilasafe.write_rsa(outfile, public)
    # create RSA object
    loaded = utilasafe.load_rsa(outfile)
    assert loaded == expected
