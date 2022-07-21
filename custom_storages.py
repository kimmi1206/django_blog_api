from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticFileStorage(S3Boto3Storage):  # pylint: disable=abstract-method
    location = settings.STATICFILES_FOLDER


class MediaFileStorage(S3Boto3Storage):  # pylint: disable=abstract-method
    location = settings.MEDIAFILES_FOLDER
