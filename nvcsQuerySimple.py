import urllib
import requests
import json

uri="https://vpc-bcb-elasticsearch-6465hlavaogxyom2nsuozai7qu.us-west-2.es.amazonaws.com/usnvc/_search"

params=json.dumps({"from": 0, "size": 10, "query": {"match": {"data.parent": {"query": "899641"}}}, "sort": [{"_id": {"order": "asc"}}]})

response = requests.get(headers={"content-type": "application/json"}, url=uri, data=params)
results = response.json()
print(results)
