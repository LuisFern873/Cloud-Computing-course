import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    body = json.loads(event['Records'][0]['body'])
    image_path = json.loads(body['Message'])
    bucket_name = 'luisfmendezl-images'
    
    rekognition = boto3.client('rekognition')
    
    labels_response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_path
            }
        },
        MaxLabels=10
    )
    
    labels = labels_response['Labels']
    tags = [label['Name'] for label in labels]

    celebrities_response = rekognition.recognize_celebrities(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_path
            }
        }
    )
    
    if 'CelebrityFaces' in celebrities_response:
        celebrities = celebrities_response['CelebrityFaces']
        for celebrity in celebrities:
            name = celebrity['Name']
            tags.append(name)
            print('Detected celebrity:', name)
    else:
        print('No celebrities detected.')
    
    # DynamoDB insertion
    user_type, user_name, image_name = image_path.split('/')
    image_user = f'{user_type}/{user_name}'
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('PostedImages')
    now = datetime.now()
    
    image = {
        'image_user': image_user,
        'image_name': image_name,
        'tags': tags,
        'image_details': {
            'posting_date': str(now.date()),
            'posting_time': str(now.time())
        }
    }
    
    print(image)
    response = table.put_item(Item=image)

    return {
        'statusCode': 200,
        'body': response
    }