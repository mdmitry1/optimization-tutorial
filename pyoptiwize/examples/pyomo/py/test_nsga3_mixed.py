# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from nsga3_mixed import main
from os import remove, popen
from os.path import exists, realpath, dirname
from sys import version
from os import getenv

def test_nsga3_mixed(monkeypatch, request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        print("")
        m.setattr(sys, 'argv', ['nsga3_mixed'])
        res = main(test_path)
        assert res == "ec3bc25d86512153a5761ded911ef78b03890b6b107810d3cb833cd8db6770db" or \
               res == "f41b42e3881c79c7582e0fda52cbb8748b9563951e1b3a172b7db65e98f153fa"
