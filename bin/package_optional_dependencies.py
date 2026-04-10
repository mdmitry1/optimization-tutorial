#!/usr/bin/env python
from pkginfo import Wheel
from sys import argv
from os.path import realpath, basename

def get_optional_dependencies(wheel_path):
    w = Wheel(wheel_path)
    # Filter for requirements that have an 'extra' marker
    optional = [req for req in w.requires_dist if 'extra ==' in req]
    return optional

# Usage
script_name = basename(realpath(argv[0]))
if len(argv) < 2:
    print(f"\nUsage: {script_name} <wheel_path>\n")
else:
    try: 
        deps = get_optional_dependencies(argv[1])
        for d in deps:
            print(d.split(';')[0])
    except Exception as err:
        print(f"\n{script_name}: ERROR: {err}\n")
        exit(1)
