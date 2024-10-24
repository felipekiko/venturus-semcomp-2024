import json
import boto3
import random

# Inicializa o cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kiko-pokemon')

def lambda_handler(event, context):
    # Scan da tabela para obter todos os items
    response = table.scan()
    items = response['Items']
    
    # Escolhe um item aleatório
    random_item = random.choice(items)
    
    # Cria a estrutura de resposta no formato desejado
    pokemon_response = {
        "id": random_item["id"],
        "name": random_item["nome"],
        "types": [
            { "type": { "name": random_item["tipo"] }}
        ],
        "sprites": {
            "front_default": random_item["foto_url"]
        }
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS,POST,PUT,DELETE',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
        },
        'body': json.dumps(pokemon_response)
    }
