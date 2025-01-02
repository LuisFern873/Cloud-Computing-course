import boto3

def lambda_handler(event, context):
    
    # JSON processing
    
    user_type = event['user_type']
    user_name = event['user_name']
    user_data = event['user_data']
    
    # DynamoDB update
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'user_type': user_type,
            'user_name': user_name
        },
        UpdateExpression="set user_data=:user_data",
        ExpressionAttributeValues={
            ':user_data': user_data
        },
        ReturnValues="UPDATED_NEW"
    )
    
    return {
        'statusCode': 200,
        'response': response
    }









