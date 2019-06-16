
from minio import Minio
import json

def main():
    minioClient = Minio('localhost:9000',
                  access_key='dalongapp',
                  secret_key='dalongapp',
                  secure=False)
    for bucket in minioClient.list_buckets():
        print(bucket)   

if __name__ == '__main__':
    main()
