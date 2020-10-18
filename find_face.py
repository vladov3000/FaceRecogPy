#!/usr/bin/env python
"""
Python Script that takes image path as input and prints the bounding box 
coordinates in JSON.
"""

import json
import sys

import face_recognition


def main(input_image_filepath: str) -> str:
    image = face_recognition.load_image_file(input_image_filepath)
    face_locations = face_recognition.face_locations(image)
    return json.dumps({"face_locations": face_locations})


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
    print(main(sys.argv[1]))
