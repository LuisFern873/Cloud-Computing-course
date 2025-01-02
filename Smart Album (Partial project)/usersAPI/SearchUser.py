import boto3

def lambda_handler(event, context):
    
    # JSON processing
    user_type = event['user_type']
    user_name = event['user_name']
    
    # DynamoDB searching
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    response = table.get_item(
        Key={
            'user_type': user_type,
            'user_name': user_name
        }
    )
    
    return {
        'statusCode': 200,
        'response': response
    }
