import requests
import datetime as dt

headers = {"Content-Type": "application/json"}
URL="http://localhost:8983/solr/admin/collections?action=LIST&wt=json"
response = requests.get(URL)
print(response.text)

