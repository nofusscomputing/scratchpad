#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from commits import Commits

def main():

    commits = Commits()

    if commits.check():
        sys.exit(0)
    else:
        sys.exit(1)
