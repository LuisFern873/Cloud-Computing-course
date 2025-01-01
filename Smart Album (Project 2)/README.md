# *Smart Album*

## Caso de uso
*Smart Album*  es  una  aplicación  serverless  Multi-tenancy con Arquitectura basada en eventos capaz de  automáticamente  organizar  fotografías  en  basea  objetos,  escenas  y  personas.  Este  utiliza  Amazon Rekognition  para  etiquetar  y  categorizar  las imágenes  subidas  en  un  bucket  de  Amazon  S3  y guardar  la  metadata  en  Amazon DynamoDB  cuando  el usuario lo requiera.

<img src="images/mental-health.png" alt="drawing" width="200"/>

<img src="images/book.png" alt="drawing" width="200"/>

## Servicios utilizados

- **Development:** Lambda, API Gateway
- **Storage:** S3
- **Database:** DynamoDB
- **Messaging:** SQS, SNS
- **AI:** Rekognition
- **Security:** KMS

## Diagrama de solución "Smart Album" serverless app

<img src="images/solution.png" alt="drawing"/>

## Amazon S3 Bucket

## Tablas DynamoDB

## Amazon API Gateway

## Lambdas

## SNS

## SQS