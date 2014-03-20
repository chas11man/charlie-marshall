from storages.backends.s3boto import S3BotoStorage
from django.conf import settings

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static', bucket=settings.AWS_BUCKET_NAME)
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media', bucket=settings.AWS_BUCKET_NAME)
