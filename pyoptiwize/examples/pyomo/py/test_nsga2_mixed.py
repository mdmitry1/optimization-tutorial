# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from nsga2_mixed import main
from os import remove, popen
from os.path import exists, realpath, dirname
from sys import version_info
from os import getenv

def test_nsga2_mixed(monkeypatch, request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        print("")
        m.setattr(sys, 'argv', ['nsga2_mixed'])
        res =  main(test_path)
        assert res == "3dcc4ef3a5fea092570ec4ec29249bd3f73849aac99294a9c0923b25e1381ee7" or \
               res == "acfd6b4d8b5bc203779b89cd6d663ee37347936d3a7d6626750ce04818d9d906" or \
               res == "6093e7449ae60a4193e9a279587b8875a528002b9e0115dcfdb2e223d51018fa" or \
               res == "24cfcd3dd7d9503c953f5dfd519bd38553cc90fec06f96458cc63d7f03519d8b"

