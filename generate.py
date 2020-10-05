#!/usr/bin/env python

""" generate.py: Prints out the flag, given the credential file.
    author: Nick S. Yu
"""

import json
import os
import sys

CYPHER_FILE_PATH = "./.cypher"
CREDENTIAL_FILE_PATH = "./.credential"

def decode_char(x,y):
    """ Sums two characters' according to their place in the
    alphabet.  For instance, a = 0, b = 1, and so on..."""
    x = ord(x) - ord('a')
    y = ord(y) - ord('a')
    return chr(ord('a') + ((x + y) % 26))

def decode_flag(credential, cypher):
    """ Decode the flag, given the given credential.  Applies
    decode_char() to every letter in the cypher and the credential."""
    ret = []
    for i in range(len(credential)):
        ret.append(decode_char(credential[i], cypher[i]))
    return "".join(ret)

def read_credential_file():
    """ Reads the contents of the current directory's .credential
    file."""
    with open(CREDENTIAL_FILE_PATH) as f:
        credential = f.read().strip()
        if len(credential) != 23:
            raise Exception("Invalid credential file.")
        print("Valid credential at {} found!".format(CREDENTIAL_FILE_PATH))
        return credential

def read_cypher_file():
    """ Reads the contents of the current directory's .credential
    file."""
    with open(CYPHER_FILE_PATH) as f:
        credential = f.read().strip()
        if len(credential) != 23:
            raise Exception("Invalid cypher file.")
        print("Valid cypher file at {} found!".format(CYPHER_FILE_PATH))
        return credential

def main():
    """ The entry point to the script."""
    print(" --- welcome to generate.py ---")

    try:
        cypher = read_cypher_file()
        credential = read_credential_file()
    except IOError:
        print("I don't have all the files I need!  GOODBYE!!!!")
        return 1

    print("The flag is: \"{}\".  Goodbye!".format(decode_flag(credential, cypher)))

    return 0

if __name__ == "__main__":
    sys.exit(main())
