import json
from querys import editEva

def lambda_handler(event: dict, context):
    method = event["requestContext"]["http"]["method"]
    if method == "PUT":
        return editData(event)
    
    return {
        'statusCode': 400,
        'body': json.dumps({'status': False})
    }

def verifyBodyPut(event: dict) -> bool:
    if event.get("body") is not None:
        body: dict = json.loads(event["body"])
        if body.get("rut") is None: return False
        if body.get("eva3") is None: return False
        return True
    return False

def editData(event: dict):
    if verifyBodyPut(event) is False: 
        return {
            'statusCode': 400,
            'body': json.dumps({'status': False})
        }
    
    body = json.loads(event["body"])
    succes = editEva(body["rut"], body["eva3"])
    return {
        'statusCode': 200,
        'body': json.dumps({'status': succes})
    }