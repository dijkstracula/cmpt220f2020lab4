#!/usr/bin/env python

""" generate.py: Prints out the flag, given the credential file.
    author: Nick S. Yu
"""

import json
import os
import sys

CREDENTIAL_FILE_PATH = "./.credentials"

def read_credential_file():
    """ Reads the contents of the current directory's .credential
    file."""
    with open(CREDENTIAL_FILE_PATH) as f:
        credential = f.read()
        if len(credential) != 16:
            raise Exception("Invalid credential file.")
        return credential

def main():
    """ The entry point to the script."""
    print(" --- generate.py ---")
    credential = read_credential_file()
    return 0

if __name__ == "__main__":
    sys.exit(main())
