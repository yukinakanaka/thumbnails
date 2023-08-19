import os
import sys
import uuid

import boto3
from PIL import Image


def create_thumnail(
    source_bucket: str, source_key: str, upload_bucket: str, upload_key: str
) -> None:
    print(
        f"""INPUT:
    source_bucket:  {source_bucket}
    source_key:     {source_key}
    upload_bucket:  {upload_bucket}
    upload_key:     {upload_key}
    """
    )
    s3_client = boto3.client("s3")
    download_local_path: str = "/tmp/{}{}".format(
        uuid.uuid4(), source_key.replace("/", "")
    )
    upload_local_path: str = "/tmp/resized-{}".format(source_key.replace("/", ""))
    s3_client.download_file(source_bucket, source_key, download_local_path)
    resize_image_locally(download_local_path, upload_local_path)
    s3_client.upload_file(upload_local_path, upload_bucket, upload_key)
    print("Succeeded!")


def resize_image_locally(image_path: str, resized_path: str) -> None:
    with Image.open(image_path) as image:
        image.thumbnail(tuple(int(x / 2) for x in image.size))  # type: ignore
        image.save(resized_path)


if __name__ == "__main__":
    source_bucket: str = sys.argv[1]
    source_key: str = sys.argv[2]
    upload_bucket: str = os.environ["UPLOAD_BUCKET"]
    upload_key: str = f"resized-{source_key}"
    create_thumnail(source_bucket, source_key, upload_bucket, upload_key)
