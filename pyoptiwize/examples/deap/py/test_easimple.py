# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from easimple_ex import main
from os import remove, popen
from os.path import exists, realpath, dirname
from sys import version
from os import getenv

def test_easimple(monkeypatch, request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        out  = test_path + '/products_ga.csv'
        out1 = test_path + '/requirements_ga.csv'
        out2 = test_path + '/resources_ga.csv'
        for o in [out, out1]:
            if exists(out):
                remove(out)
        assert exists(out) == False
        print("")
        m.setattr(sys, 'argv', ['easimple_ex'])
        assert main(test_path) == "bfeabc4b3f30ef63488fcbdef55ba7e67c019f7361463e97ff6ccc801ca0ef5f"
        assert int(popen(f"sum {out}").read().split()[0])  == 20585
        assert int(popen(f"sum {out1}").read().split()[0]) == 32435
        assert int(popen(f"sum {out2}").read().split()[0]) == 33263
