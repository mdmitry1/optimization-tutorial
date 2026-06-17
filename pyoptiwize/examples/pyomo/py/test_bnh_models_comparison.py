# Copyright (C) 2025-2026 Dmitry Messerman
# SPDX-License-Identifier: GPL-3.0

import sys
from bnh_models_comparison import main
from os import remove, popen
from os.path import exists, realpath, dirname
from sys import version
from os import getenv

def test_bnh_models_comparison(monkeypatch, request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        print("")
        m.setattr(sys, 'argv', ['bnh_models_comparison'])
        result = main(test_path)
        assert result == "0bba1875c7fa2f11bc2118e234372fa5ad8ec2c1e8de0692b23358d45624a3c9" or \
               result == "7f5b6fc931c0c6e75b059d23b28707b9de67032ce282bd5606a262270c539b2e" or \
               result == "416bff1331db1a4fd69f393adedff355b871a7e2ac2301b5eedb2347fd883a97"
