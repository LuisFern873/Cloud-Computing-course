import boto3

def lambda_handler(event, context):
    
    user_type = event['user_type']
    user_name = event['user_name']
    image_user = f'{user_type}/{user_name}'
    
    image_name = event['image_name']
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PostedImages')

    dynamodb_response = table.delete_item(
        Key={
            'image_user': image_user,
            'image_name': image_name
        }
    )
    
    return {
        'statusCode': 200,
        'response': dynamodb_response
    }




