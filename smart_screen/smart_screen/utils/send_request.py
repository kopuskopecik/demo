import requests

def send_request(method, url, headers = None, data = None, files = None):
    res = requests.request(method, url, headers=headers, data=data, files=files, verify=False)
    try:
        data = res.json()
    except:
        data = res.content

    return data, res.status_code