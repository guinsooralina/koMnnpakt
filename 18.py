import boto3
from botocore.client import Config

ACCESS_KEY = "ВАШ_ИДЕНТИФИКАТОР_КЛЮЧА"
SECRET_KEY = "ВАШ_СЕКРЕТНЫЙ_КЛЮЧ"

s3_client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(region_name='ru-central1', signature_version='s3v4')
)

# Загрузка файла
s3_client.upload_file('image.png', 'my-bucket', 'image.png')
