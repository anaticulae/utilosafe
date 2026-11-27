#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import importlib.metadata
import os

__version__ = importlib.metadata.version('utilosafe')

from utilosafe.password import decrypt as decrypt_aes
from utilosafe.password import encrypt as encrypt_aes
from utilosafe.public import decrypt as decrypt_rsa
from utilosafe.public import encrypt as encrypt_rsa
from utilosafe.rsa import create_private_key
from utilosafe.rsa import create_public_key
from utilosafe.rsa import load_rsa_private
from utilosafe.rsa import load_rsa_public
from utilosafe.rsa import write_rsa
from utilosafe.utils import UTILOSAFE_PUBLIC_KEY
from utilosafe.utils import UTILOSAFE_USER_PASSWORD
from utilosafe.utils import public_password
from utilosafe.utils import user_password

# TODO: MAY REMOVE LATER?
decrypt_password = decrypt_aes
encrypt_password = encrypt_aes

decrypt = decrypt_aes
encrypt = encrypt_aes

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
