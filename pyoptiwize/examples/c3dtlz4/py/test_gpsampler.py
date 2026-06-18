# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from c3dtlz4_ex import main
from os import remove, popen
from os.path import exists, realpath, dirname
from sys import version_info
from os import getenv

def test_gpsampler(monkeypatch, request):
    root_dir = str(request.config.rootpath) + "/"
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        out =  test_path + '/results.csv'
        if exists(out):
            remove(out)
        print("")
        assert exists(out) == False
        m.setattr(sys, 'argv', ['c3dtlz4_ex','-n','100','-p',test_path])
        assert main() == 'e888305e3b5d5d09eccefd53e750e89aa77496deacb60f59c615f4cbd67edba3'
        if version_info.minor == 14:
            assert int(popen(f"sum {out}").read().split()[0]) == 35272 or \
                   int(popen(f"sum {out}").read().split()[0]) == 38273
        else:
            assert int(popen(f"sum {out}").read().split()[0]) == 47204 or \
                   int(popen(f"sum {out}").read().split()[0]) == 10640 or \
                   int(popen(f"sum {out}").read().split()[0]) == 35272 or \
                   int(popen(f"sum {out}").read().split()[0]) == 45261 or \
                   int(popen(f"sum {out}").read().split()[0]) == 52597 or \
                   int(popen(f"sum {out}").read().split()[0]) == 33613
