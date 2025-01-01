import boto3

def lambda_handler(event, context):
    
    user_type = event['user_type']
    user_name = event['user_name']
    
    # Delete user from Users
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')

    dynamodb_response = table.delete_item(
        Key={
            'user_type': user_type,
            'user_name': user_name
        }
    )
    
    # Delete folder from the Bucket
    bucket_name = 'luisfmendezl-images'
    prefix = f'{user_type}/{user_name}/'

    s3 = boto3.client('s3')
    s3_response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    print(s3_response)

    if 'Contents' in s3_response:
        objects = [{'Key': obj['Key']} for obj in s3_response['Contents']]
        s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
    
    # Delete their images from PostedImages
    dynamodb = boto3.client('dynamodb')
    image_user = f'{user_type}/{user_name}'
    
    scan_params = {
        'TableName': 'PostedImages',
        'FilterExpression': 'image_user = :image_user',
        'ExpressionAttributeValues': {
            ':image_user': {'S': image_user}
        }
    }

    response = dynamodb.scan(**scan_params)

    for item in response['Items']:
        delete_params = {
            'TableName': 'PostedImages',
            'Key': {
                'image_user': item['image_user'],
                'image_name': item['image_name']
            }
        }
        dynamodb.delete_item(**delete_params)
    
    return {
        'statusCode': 200,
        'response': dynamodb_response
    }




