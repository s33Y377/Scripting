import requests

url = "http://192.168.16.153:8000/bluescope/api/agent/test"
try:
    requests.get(url, timeout=1)
except BaseException as e:
    print(str(e))
