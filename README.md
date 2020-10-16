# FaceRecogPy

Set of scripts to use in backend of Face Recognition App.

Setup:

    python3 -m venv ./venv
    source venv/bin/activate
    pip install -r requirements.txt

Test it out:

    python find_face.py test_images/obama.jpg

    python save_face.py test_images/romney.jpg romney
    python save_face.py test_images/obama2.jpg obama2
    python save_face.py test_images/obama1.jpg obama1

    python match_face.py test_images/obama.jpg
