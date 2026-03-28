# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import utilo
import utilosafe.rsa

import utilosafe


def main():
    cwd = os.getcwd()
    password = insert_password()

    path_private = os.path.join(cwd, 'private.pem')
    private = utilosafe.rsa.create_private_key(passphrase=password)
    utilo.log(f'write private: {path_private}')
    utilosafe.write_rsa(path_private, private)

    path_public = os.path.join(cwd, 'public.pem')
    public = utilosafe.rsa.create_public_key(private, passphrase=password)
    utilo.log(f'write public: {path_public}')
    utilosafe.write_rsa(path_public, public)

    sys.exit(utilo.SUCCESS)


def insert_password():
    password = input('password\n')
    if password:
        password = password.strip()
        password = password.encode('utf8')
    else:
        password = None
    return password
