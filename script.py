import requests

# print(sys.version)
print(sys.executable)


r = requests.get("http://coreyms.com")
print(r.status_code)
