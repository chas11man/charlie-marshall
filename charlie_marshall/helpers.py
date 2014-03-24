from storages.backends.s3boto import S3BotoStorage
from django.conf import settings

class FixedS3BotoStorage(S3BotoStorage):
	def __init__(self, *args, **kwargs):
		super(FixedS3BotoStorage, self).__init__(bucket=settings.AWS_BUCKET_NAME, *args, **kwargs)

	def url(self, name):
		url = super(FixedS3BotoStorage, self).url(name)
		bucket_name = self.bucket.name
		if "%s.s3.amazonaws.com" % bucket_name in url:
			url = url.replace("%s.s3.amazonaws.com/" % bucket_name, "s3.amazonaws.com/%s/" % bucket_name)
		return url

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
