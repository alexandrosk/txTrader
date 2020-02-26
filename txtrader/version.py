#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  version.py
  ----------

  TxTrader version module 

  Copyright (c) 2015 Reliance Systems Inc. <mkrueger@rstms.net>
  Licensed under the MIT license.  See LICENSE for details.

"""

VERSION_MAJOR = 1
VERSION_MINOR = 11 
VERSION_PATCH = 0
BUILD=2385
DATE='2020-02-26'
TIME='12:24:42'
VERSION = '%s.%s.%s' % (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
DATETIME = '%s %s' % (DATE, TIME)
LABEL = 'TxTrader Securities Trading API Controller'
HEADER = '%s %s (build %s) %s' % (LABEL, VERSION, BUILD, DATETIME)
COMMIT='commit d790b5d327d5a6464292859c225dfffe9837b625 (HEAD -> refs/heads/v1.11.0-dev, refs/remotes/origin/v1.11.0-dev)'
