import sys
from scip import main
from os import remove, popen
from os.path import realpath, dirname
from sys import version
from os import getenv

def test_scip(monkeypatch, request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0]))
        print("")
        m.setattr(sys, 'argv', ['scip'])
        result = main(test_path,5000)
        assert result == "0f040f58a8717972b61635ca53dcf5b457303d62f8afe14513a78fc9d18c1299"
