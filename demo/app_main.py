"""
    Self defined file -Yiyun
"""
import requests
import webbrowser
AppKey = '6d3F1VV1gymPdxKtVs39tFqXrVQG4VbY'
AppID = '29976929'
SecretKey = 'sSryrMwj4wYWVLnocgUUKuAUUzkyoGxG'
Redirect_url = 'oob'

def get_code_manually():

    url = 'http://openapi.baidu.com/oauth/2.0/authorize?'\
        'response_type=code&'\
        F'client_id={AppKey}&'\
        F'redirect_uri={Redirect_url}&'\
        'scope=basic,netdisk&'\
        F'device_id={AppID}'

    webbrowser.open(url, new=0, autoraise=True)

code = 'db1a20c1a0e1c49a8cd32b5d5cdf1acc'

url_access_get = 'https://openapi.baidu.com/oauth/2.0/token?'\
    'grant_type=authorization_code&'\
    F'code={code}&'\
    F'client_id={AppKey}&'\
    F'client_secret={SecretKey}&'\
    F'redirect_uri={Redirect_url}'

resp = requests.get(url_access_get)
data = resp.json()
print(data)
access_token = data['access_token']

