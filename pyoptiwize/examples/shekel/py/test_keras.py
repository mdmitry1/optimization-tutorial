#!/usr/bin/env python3.12

# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from os import remove, popen
from os.path import exists, realpath, dirname
from os import getenv
from pytest import mark

@mark.skipif(sys.version_info >= (3, 14), 
        reason="Skipping Keras tests for Python 3.14")
def test_keras(monkeypatch, request):
    from keras_ex import main
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        print("")
        m.setattr(sys, 'argv', ['keras_ex'])
        result = main(512, test_path)
        assert result == '3be173406872257840c43d3c0a15f1115a87dd1145eac802b893832501ea3b60' or \
               result == 'd353c09d5636cc3ca3e92fd0f2d35da421d6755d9708db8fb819639661574589'
