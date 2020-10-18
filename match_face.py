#!/usr/local/bin/python
"""
Python script that takes input image, encodes it, and compares encoding 
to saved encodings. Prints id of the most similiar encoding or "" if 
there are no saved encodings or the min difference between the face encodings
is larger than the tolerance.
"""

import os
import pickle
import sys

import face_recognition

from context import SAVED_ENCODINGS_DIR

MATCH_TOLERANCE = 0.6


def main(input_image_filepath: str, debug: bool = False) -> str:
    if not os.path.isdir(SAVED_ENCODINGS_DIR):
        return ""

    input_image = face_recognition.load_image_file(input_image_filepath)
    input_image_encoding = face_recognition.face_encodings(input_image)[0]

    min_diff = None
    best_id = None
    for filename in os.listdir(SAVED_ENCODINGS_DIR):
        saved_image_path = os.path.join(SAVED_ENCODINGS_DIR, filename)
        with open(saved_image_path, "rb") as f:
            saved_image_encoding = pickle.load(f)

        diff = face_recognition.face_distance(
            [input_image_encoding], saved_image_encoding
        )[0]

        if min_diff == None or diff < min_diff:
            min_diff = diff
            best_id = os.path.splitext(filename)[0]

        if debug:
            print(f"{filename}: {diff}")

    if min_diff > MATCH_TOLERANCE:
        return ""

    return best_id


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    print(main(sys.argv[1]))
