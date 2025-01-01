import json
import boto3

def lambda_handler(event, context):
    
    # JSON processing
    user_type = event['user_type']
    user_name = event['user_name']
    user_data = event['user_data']
    
    user = {
        'user_type': user_type,
        'user_name': user_name,
        'user_data': user_data
    }
    
    # S3 bucket creation
    s3_client = boto3.client('s3')
    bucket_name = 'luisfmendezl-images'
    folder_name = f'{user_type}/{user_name}/' 

    s3_response = s3_client.put_object(
        Bucket=bucket_name,
        Key=(folder_name)
    )
    print(s3_response)
    
    # SNS publication
    sns_client = boto3.client('sns')
    sns_response = sns_client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:896823805584:NewUser',
        Subject = 'New user',
        Message = json.dumps(user),
        MessageAttributes = {
            'user_type': {'DataType': 'String', 'StringValue': user_type }
        }
    )
    
    return {
        'statusCode': 200,
        'body': sns_response
    }



