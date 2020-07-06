from flask import Flask
import requests


def checkRequest(url: str, token: str):

    check_json = None

base_url = "http://api.postmon.com.br/v1/cep/30170010"

response = requests.get(base_url)
data = response.json

if response.status_code == 200:
    print('Check == ', response.status_code)
else:
    print('Down', response.status_code)


####################################################################

app = Flask("Health-Check")

@app.route('/', methods=['GET'])
def hc():
    return 'HealthCheck-API', 200

if __name__=='__main__':
    app.run(debug=True)

