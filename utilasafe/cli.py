# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import utila

import utilasafe
import utilasafe.rsa


def main():
    cwd = os.getcwd()

    password = input('password\n')
    password = password.strip() if password else None

    path_private = os.path.join(cwd, 'private.pem')
    private = utilasafe.rsa.create_private_key(passphrase=password)
    utila.log(f'write private: {path_private}')
    utilasafe.write_rsa(path_private, private)

    path_public = os.path.join(cwd, 'public.pem')
    public = utilasafe.rsa.create_public_key(private, passphrase=password)
    utila.log(f'write public: {path_public}')
    utilasafe.write_rsa(path_public, public)

    sys.exit(utila.SUCCESS)
