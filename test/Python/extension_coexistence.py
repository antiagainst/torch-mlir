# Some checks that we can import the various extensions and libraries and
# not have symbol collisions or other goings on.
# RUN: %PYTHON %s

import sys

print(f"PYTHONPATH={sys.path}")

import mlir.ir
import npcomp

print("Extensions all loaded")
