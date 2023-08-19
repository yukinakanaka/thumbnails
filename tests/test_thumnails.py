from os import path

from src.thumnails import create_thumnail, resize_image_locally


def test_resize_image():
    image_path = path.join(path.dirname(__file__), "test.jpg")
    resized_path = path.join(path.dirname(__file__), "resized-test.jpg")
    resize_image_locally(image_path, resized_path)


def test_create_thumnail():
    """
    Please set your AWS creadentials in Environment varivales when you run pytrest
    Example:
        export AWS_ACCESS_KEY_ID=xxx
        export AWS_SECRET_ACCESS_KEY=xxx
        pytest
    """

    """
    Please set your test bucket's name
    Example:
        create_thumnail(
            "argo-events-s3-trigger-nakamura",
            "test.jpg",
            "argo-events-s3-trigger-nakamura-upload",
            "resized-test.jpg",
        )
    """

    create_thumnail(
        "YOUR_SOURCE_BUCKET_NAME",
        "YOUR_TEST_FILE_NAME",
        "YOUR_UPLOAD_BUCKET_NAME",
        "YOUR_UPLOAD_TEST_FILE_NAME",
    )
