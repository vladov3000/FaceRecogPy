#!/usr/local/bin/python
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
SAVED_ENCODINGS_DIR = os.path.join(BASE_PATH, "saved_encodings")

if not os.path.isdir(SAVED_ENCODINGS_DIR):
    os.mkdir(SAVED_ENCODINGS_DIR)
