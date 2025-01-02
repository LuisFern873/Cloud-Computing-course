import json
import boto3

def lambda_handler(event, context):
    
    # JSON processing
    user_type = event['user_type']
    user_name = event['user_name']
    image_user = f'{user_type}/{user_name}'
    
    # Create a DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Define the search parameters
    search_params = {
        'TableName': 'PostedImages',
        'FilterExpression': 'image_user = :image_user',
        'ExpressionAttributeValues': {
            ':image_user': {'S': image_user}
        }
    }

    # Perform the search query
    response = dynamodb.scan(**search_params)

    # Extract the matching items
    items = response.get('Items', [])

    for item in items:
        item.pop('image_user', None)
        item.pop('tags', None)
    
    return {
        'statusCode': 200,
        'body': items
    }