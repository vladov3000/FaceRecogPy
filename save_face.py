"""
Python script that will save encoding of picture of face given filepath to image and image id.
Prints "Cannot encode" if no encoding found.
"""

import os
import pickle
import shutil
import sys

import face_recognition

from context import SAVED_ENCODINGS_DIR


def main(image_path: str, id: str) -> str:
    if not os.path.isdir(SAVED_ENCODINGS_DIR):
        os.mkdir(SAVED_ENCODINGS_DIR)

    _, suffix = os.path.splitext(image_path)
    save_path = os.path.join(SAVED_ENCODINGS_DIR, f"{id}.dat")

    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)
    if encoding == []:
        return "Cannot encode"

    with open(save_path, "wb") as f:
        pickle.dump(encoding[0], f)
    return ""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()
    print(main(sys.argv[1], sys.argv[2]))
