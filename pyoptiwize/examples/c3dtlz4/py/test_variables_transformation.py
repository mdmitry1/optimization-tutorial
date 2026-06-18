# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from transform_variables import main
from os import remove, popen
from os.path import exists, realpath, dirname
from os import getenv

def test_variables_transformation(monkeypatch, request):
    root_dir = str(request.config.rootpath) + "/"
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        out =  test_path + '/transformed_variables.csv'
        if exists(out):
            remove(out)
        print("")
        assert exists(out) == False
        m.setattr(sys, 'argv', ['transform_variables','-db','example_expected.db', '-r','results_expected.csv','-p',test_path])
        assert main() == 'a4dd5156b52f55a86385db21ed3495fb9e3b49845e7839fcdf14ebb72d83ca08'
        assert int(popen(f"sum {out}").read().split()[0]) == 28924
