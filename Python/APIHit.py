import requests


def requ():
    response = requests.get(url="http://api.github.com")
    print(response.text)


requ()
