import sys
import uuid

import boto3
from PIL import Image


def create_thumnail(source_bucket: str, source_key: str, upload_bucket: str) -> None:
    s3_client = boto3.client("s3")
    download_local_path: str = "/tmp/{}{}".format(
        uuid.uuid4(), source_key.replace("/", "")
    )
    upload_local_path: str = "/tmp/resized-{}".format(source_key.replace("/", ""))
    s3_client.download_file(source_bucket, source_key, download_local_path)
    resize_image_locally(download_local_path, upload_local_path)
    s3_client.upload_file(
        upload_local_path, upload_bucket, "resized-{}".format(source_key)
    )


def resize_image_locally(image_path: str, resized_path: str) -> None:
    with Image.open(image_path) as image:
        image.thumbnail(tuple(int(x / 2) for x in image.size))  # type: ignore
        image.save(resized_path)


if __name__ == "__main__":
    source_bucket: str = sys.argv[1]
    source_key: str = sys.argv[2]
    upload_bucket: str = sys.argv[3]
    create_thumnail(source_bucket, source_key, upload_bucket)
