#!/usr/bin/env python
import subprocess
import sys

def main(argv):
  subprocess.call(["wget", "-m", "-k", "-K", "-E", "http://www.chromium.org"])

if __name__ == '__main__':
  sys.exit(main(sys.argv))



