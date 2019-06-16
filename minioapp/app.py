
import boto3


def main():
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id='dalongapp',
        aws_secret_access_key='dalongapp',
        endpoint_url='http://localhost:9000',
    )
    print(s3_client.list_buckets())


if __name__ == '__main__':
    main()
