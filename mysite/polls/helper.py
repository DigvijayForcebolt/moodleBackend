import requests

def access_token_sf():
    url = "https://chefannfoundation--appststng.sandbox.my.salesforce.com/services/oauth2/token?grant_type=refresh_token&client_id=3MVG9wLr_6EJB3zCYw7SwN0JQ4puLgqRXAXbASCrqiLH_SVZKZ7TnRcUYdHZzm1uw8j1XH1vqdZ78vB8BxrdN&client_secret=7D4385337ACCB507928AFED37CBF34DD423EE7578F695ACA1A1E0104803B888C&refresh_token=5Aep861K29sXrAChqucCvb17C0c73uuX9jIA8Jqjg3VgMClxz.qft4Aezwwt3XQif_D6ner_0AvzwQdjg6bTC_Z"

    payload={}
    headers = {
    'Cookie': 'BrowserId=YUyLN2D6Ee2G3o9btM0jvg; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    access_token = response.get('access_token')
    return access_token
