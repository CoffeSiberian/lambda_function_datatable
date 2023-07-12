import json
from querys import insertData, selectData

def lambda_handler(event: dict, context):
    method = event["requestContext"]["http"]["method"]
    if method == "GET":
        return getData()
    elif method == "POST":
        return postData(event)
    
    return {
        'statusCode': 400,
        'body': json.dumps({'status': False})
    }

def getData():
    data = selectData()
    return {
        'statusCode': 200,
        'body': json.dumps({'data': data})
    }

def postData(event: dict):
    if verifyBodyPost(event) is False: 
        return {
            'statusCode': 400,
            'body': json.dumps({'status': False})
        }
    
    body = json.loads(event["body"])
    succes = insertData(body["rut"], body["nombre"], body["apellido"], body["celular"])
    return {
        'statusCode': 200,
        'body': json.dumps({'status': succes})
    }

def verifyBodyPost(event: dict) -> bool:
    if event.get("body") is not None:
        body: dict = json.loads(event["body"])
        if body.get("rut") is None: return False
        if body.get("nombre") is None: return False
        if body.get("apellido") is None: return False
        if body.get("celular") is None: return False
        return True
    return False