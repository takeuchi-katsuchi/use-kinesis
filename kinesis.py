import boto3

client = boto3.client(
    'firehose',
    aws_access_key_id='AKIATPWQCJYK3RI7JOI5',
    aws_secret_access_key='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',
    region_name='ap-northeast-1'
)

response = client.put_record(
    DeliveryStreamName='Ducube-test-kinesis-firehose20210213',
    Record={
        'Data': 'Firehosetest'
    }
)

print(response)
