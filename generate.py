#!/usr/bin/env python

""" generate.py: Prints out the flag, given the credential file.
    author: Nick S. Yu
"""

import json
import os
import sys

CREDENTIAL_FILE_PATH = "./.credential"
CYPHER = 'bzssppgbtctgemlsxgiagdl'

def decode_char(x,y):
    """ Sums two characters' according to their place in the
    alphabet.  For instance, a = 0, b = 1, and so on..."""
    x = ord(x) - ord('a')
    y = ord(y) - ord('a')
    return chr(ord('a') + ((x + y) % 26))

def decode_flag(credential):
    """ Decode the flag, given the given credential. """
    return "TODO: finish this!"

def read_credential_file():
    """ Reads the contents of the current directory's .credential
    file."""
    try:
        with open(CREDENTIAL_FILE_PATH) as f:
            credential = f.read().strip()
            if len(credential) != 23:
                raise Exception("Invalid credential file.")
            return credential
    except IOError as e:
        raise Exception("No credential file found.  Contact Big Boss for one.")

def main():
    """ The entry point to the script."""
    print(" --- welcome to generate.py ---")
    credential = read_credential_file()

    print("Valid credential found!")
    print("The flag is: \"{}\".  Goodbye!".format(decode_flag(credential)))

    return 0

if __name__ == "__main__":
    sys.exit(main())
