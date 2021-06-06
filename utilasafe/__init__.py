#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

from utilasafe.password import decrypt as decrypt_password
from utilasafe.password import encrypt as encrypt_password
from utilasafe.public import decrypt as decrypt_public
from utilasafe.public import encrypt as encrypt_public
from utilasafe.rsa import load_rsa
from utilasafe.rsa import write_rsa
from utilasafe.utils import user_password

__version__ = '0.0.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
