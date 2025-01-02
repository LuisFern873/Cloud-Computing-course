import json
import boto3
import base64
from datetime import date

def lambda_handler(event, context):

    Message = event["Records"][0]["Sns"]['Message']
    Message = json.loads(Message)
    
    user_type = Message['user_type']
    user_name = Message['user_name']
    user_data = Message['user_data']

    user_data['password'] = encrypt_password(user_data['password'])

    user_data['registration_date'] = str(date.today())

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    
    user = {
        'user_type': user_type,
        'user_name': user_name,
        'user_data': user_data
    }
    print(user)
    response = table.put_item(Item=user)
    
    return {
        'statusCode': 200,
        'body': response
    }

def encrypt_password(password):
    
    kms_client = boto3.client('kms')
    response = kms_client.encrypt(
        KeyId='fa48f908-27d4-4949-9052-7340cec268fa',
        Plaintext=password
    )
    encrypted_password = response['CiphertextBlob']

    return base64.b64encode(encrypted_password).decode('utf-8')





