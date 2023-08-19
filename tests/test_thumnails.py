from os import path

from src.thumnails import create_thumnail, resize_image_locally


def test_resize_image():
    image_path = path.join(path.dirname(__file__), "test.jpg")
    resized_path = path.join(path.dirname(__file__), "resized-test.jpg")
    resize_image_locally(image_path, resized_path)


def test_create_thumnail():
    # Please set your AWS creadentials in Environment varivales when you run pytrest
    # Please set your test bucket's name
    create_thumnail(
        "YOUR_SOURCE_BUCKET_NAME",
        "YOUR_TEST_FILE_NAME",
        "YOUR_UPLOAD_BUCKET_NAME",
    )
