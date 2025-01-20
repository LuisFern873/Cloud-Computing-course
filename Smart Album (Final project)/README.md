# *Smart Album*

## Caso de uso
*Smart Album* es una aplicación serverless de arquitectura Multi-Tenancy basada en eventos, diseñada para organizar automáticamente fotografías según objetos, escenas y personas. Utiliza Amazon Rekognition para etiquetar y categorizar las imágenes cargadas en un bucket de Amazon S3, almacenando la metadata en Amazon DynamoDB de forma dinámica, según las necesidades del usuario.


<p align="center">
  <img src="images/mental-health.png" style="width: 150px; height: auto; padding: 10px"> 
  <img src="images/book.png" style="width: 150px; height: auto; padding: 10px">
</p>

## Servicios utilizados

- **Development:** Lambda, API Gateway
- **Storage:** S3
- **Database:** DynamoDB
- **Messaging:** SQS, SNS
- **AI:** Rekognition
- **Security:** KMS

## Diagrama de solución

<img src="images/solution.png" alt="drawing" style="display: block; margin: auto;"/>
