# Thumbnails
- A thumnail creater: It will download a file from a source s3 bucket and resize it, then upload it to a s3 bucket.
- Original codes is from [Tutorial: Using an Amazon S3 trigger to create thumbnail images](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html)

## Usage

### Build
```
docker build -t thumnails .
```

### RUN
Set variables
```
AWS_ACCESS_KEY_ID=aaa
AWS_SECRET_ACCESS_KEY=bbb

SOURCE_BUCKET=ccc
SOURCE_KEY=ddd

UPLOAD_BUCKET=eee
```
Run
```
docker run \
--env AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
--env AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
--env UPLOAD_BUCKET=${UPLOAD_BUCKET} \
thumnails \
${SOURCE_BUCKET} ${SOURCE_KEY}
```
example:
```
docker run \
--env AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
--env AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
--env UPLOAD_BUCKET=${UPLOAD_BUCKET} \
thumnails \
${SOURCE_BUCKET} ${SOURCE_KEY}

INPUT:
    source_bucket:  argo-events-s3-trigger-nakamura
    source_key:     test.jpg
    upload_bucket:  argo-events-s3-trigger-nakamura-upload
    upload_key:     resized-test.jpg
    
Succeeded!
```

## References
- [Tutorial: Using an Amazon S3 trigger to create thumbnail images](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html)
