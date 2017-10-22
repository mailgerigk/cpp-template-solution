from pathlib import Path
from subprocess import call
import os

dir = os.path.dirname(os.path.realpath(__file__))
exts = ["h", "hpp", "c", "cpp"]

for ext in exts:
    pathlist = Path(dir).glob("**/*." + ext)
    for path in pathlist:
        call(["clang-format", "-i", str(path)])
