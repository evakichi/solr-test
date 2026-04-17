import requests
import datetime as dt

URL="http://localhost:8983/api/collections"
headers = {"Content-Type": "application/json"}
now_str = dt.datetime.now().strftime("%Y%m%d_%H%M%S_%f")

collection_name = f"techproducts_{now_str}"

data = {"name": collection_name ,"numShards": 1,"replicationFactor": 1}
response = requests.post(URL,json=data,headers=headers)
print(response)

URL=f"http://localhost:8983/solr/{collection_name}/schema"
data={ "add-field":
      [ 
       {"name": "name", "type": "text_general", "multiValued": False}, 
       {"name": "cat", "type": "string", "multiValued": True}, 
       {"name": "manu", "type": "string"}, 
       {"name": "features", "type": "text_general", "multiValued": True}, 
       {"name": "weight", "type": "pfloat"}, 
       {"name": "price", "type": "pfloat"}, 
       {"name": "popularity", "type": "pint"}, 
       {"name": "inStock", "type": "boolean", "stored": True}, 
       {"name": "store", "type": "location"} 
       ] 
      }

response = requests.post(URL,json=data,headers=headers)
print(response)

data=  {
    "id" : "978-0641723445",
    "cat" : ["book","hardcover"],
    "name" : "The Lightning Thief",
    "author" : "Rick Riordan",
    "series_t" : "Percy Jackson and the Olympians",
    "sequence_i" : 1,
    "genre_s" : "fantasy",
    "inStock" : True,
    "price" : 12.50,
    "pages_i" : 384
  }

URL=f"http://localhost:8983/api/collections/{collection_name}/update"
response = requests.post(URL,json=data,headers=headers)
print(response)

