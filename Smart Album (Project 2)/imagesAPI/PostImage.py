import json
import boto3

def lambda_handler(event, context):

    user_type = event['user_type']
    user_name = event['user_name']
    image_name = event['image_name']

    s3_client = boto3.client('s3')
    bucket_name = 'luisfmendezl-images'
    image_path = f'{user_type}/{user_name}/{image_name}'

    try:
        s3_response = s3_client.head_object(Bucket=bucket_name, Key=image_path)

        # SNS publication
        sns_client = boto3.client('sns')

        sns_response = sns_client.publish(
            TopicArn = 'arn:aws:sns:us-east-1:896823805584:NewImage',
            Subject = 'New Image',
            Message = json.dumps(image_path),
            MessageAttributes = {
                'user_type': {'DataType': 'String', 'StringValue': user_type }
            }
        )

        return {
            'statusCode': 200,
            'body': sns_response
        }
    
    except Exception as e:

        print("Image does not exist:", str(e))
        return {
            'statusCode': 404,
            'body': 'Image not found'
        }







