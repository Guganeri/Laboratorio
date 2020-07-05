import requests
import json

def FactoryRequest(url: str, token: str):

    cat_json = None

    try:
        response = requests.get(url=url, headers={'x-api-key':token},verify=True)
        response_json = response.json()
    except Exception as exception:
        print ("Ops: Something Else",exception)
    
    return response_json