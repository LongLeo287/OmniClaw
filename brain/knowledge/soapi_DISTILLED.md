---
id: soapi
type: knowledge
owner: OA_Triage
---
# soapi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# SOAPI - Scanning OpenAPIs

Map OpenAPI documentations as Neo4J graphs and uncover vulnerabilities in the design implementation of the API. A Bloodhound for APIs.

SOAPI uses graph traversal techniques to helps you detect:
- potential sensitive data exposure
- public endpoint leaks
- rate-limiting bypasses
- parameter example values for IDOR exploitation
- data sinks  

Developed for OWASP Copenhagen 2024 and Disobey 2025 conferences - recordings coming soon!

* OWASP 2024 - [PDF Slides 2024 ](https://0xpwn.wordpress.com/wp-content/uploads/2024/09/a-deep-dive-into-openapi-security.pdf)
* Disobey 2025 - [PDF Slieds 2025](https://0xpwn.wordpress.com/wp-content/uploads/2025/02/hunting-for-attack-paths-in-openapi-documentations.pdf)

Check out the [SquareSec SOAPI Guide](https://www.sqrsec.com/soapi-guide) to see how to use it

![image](https://github.com/user-attachments/assets/bede7a1f-f5f1-4fe2-9e34-df2985cd5a69)



## 1. Installation
```
git clone https://github.com/andrei8055/SOAPI/
cd SOAPI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 soapi.py
```

## 2. Config
1. Set up your Neo4j DB (you can use the sandbox for free)
2. Extract URL, username and password
3. Place them in the `config.py` file
```
neo4j_config = {
    "uri": "bolt://127.0.0.1",
    "username": "neo4j",
    "password": "<password>"
}
```

## 3. Running
1. Drop your openapi.json file(s) in the `/samples` folder
2. Run `python3 soapi.py`
```
python3 soapi.py 

███████╗ ██████╗  █████╗ ██████╗ ██╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║
███████╗██║   ██║███████║██████╔╝██║
╚════██║██║   ██║██╔══██║██╔═══╝ ██║
███████║╚██████╔╝██║  ██║██║     ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
                                    

[------------------------------]
[+] Cleaning Neo4j DB..
[+] Neo4j DB deleted!
[+] Analyzing samples/3074.json
[+] Parsing complete!
[+] Uploading data to Neo4j server..
[+] Data uploaded succesfully!
[+] Checking vulnerable paths..
[------------------------------]

[+] Stats:

There are 25 unique endpoints
 - 14 public endpoints
 - 11 protected endpoints

[------------------------------]

[+] IDOR ID Finder:

[*] post_/v1/signin
string username
 -> post /v1/signin
 -> get /v1/check
 -> get /v1/user/:{username}

[*] post_/v1/signup
string username
 -> post /v1/signin
 -> get /v1/check
 -> get /v1/user/:{username}

[------------------------------]

[+] List objects accessible through public & private endpoints

[+] serverError
Public: post /v1/signin
Public: get /v1/user
Public: get /v1/user/:{username}
Public: get /v1/event
Public: get /v1/event/:{uuid}
Public: get /v1/multimedia/image
Public: get /v1/multimedia/video
Public: get /v1/report
Public: get /v1/report/info
Public: get /v1/stat
Protected: post /v1/signup
Protected: get /v1/check
Protected: delete /v1/user/:{username}
Protected: delete /v1/event/:{uuid}
Protected: patch /v1/event/comment
Protected: post /v1/report
Protected: patch /v1/report/info
Protected: delete /v1/report/info

[+] unsupportedMediaType415
Public: post /v1/signin
Protected: post /v1/signup
Protected: put /v1/event
Protected: patch /v1/event/comment
Protected: patch /v1/jetson/docker
Protected: patch /v1/jetson/image
Protected: post /v1/report
Protected: patch /v1/report/info
Protected: delete /v1/report/info

[------------------------------]

[+] List public readble fields

----
POST /v1/signin
[-] string accessToken
[-] string username
[-] string error
----
GET /v1/user
[-] [string] users
[-] string error
----
GET /v1/user/:{username}
[-] string username
[-] string first_name
[-] string last_name
[-] string role
[-] string error
[-] string error
----
GET /v1/event/:{uuid}
[-] string uid
[-] integer number
[-] string side
[-] integer brigade
[-] string video_path
[-] string image_path
[-] string start_time
[-] string end_time

[------------------------------]

[+] List public endpoints

post /v1/signin
get /v1/user
get /v1/user/:{username}
get /v1/event
get /v1/event/:{uuid}
get /v1/event/status
get /v1/jetson/docker
get /v1/jetson/image
get /v1/multimedia/stream
get /v1/multimedia/image
get /v1/multimedia/video
get /v1/report
get /v1/report/info
get /v1/stat
```

## 4. Analyze
1. Given a field/object - get all paths to there starting from the endpoint

```
MATCH (start), (end {uid: "UserEmail"})
WHERE start.uid STARTS WITH "path_"
MATCH path = (start)-[*..10]->(end)
RETURN path

```


2. Find path between 2 nodes

```
MATCH path = (start {uid: "User_object"})-[*1..5]-(end {uid: "UserEmail_string"})
RETURN path
```

3. Find a specific object and it's links
```
MATCH (n {uid: "Account_object"})-[r]-(connected)
RETURN n, r, connected

```


4. Delete everything from Neo4J

```
MATCH (n)
DETACH DELETE n;
```

5. View the whole OpenAPI as a graph
```
MATCH (n)
RETURN n
LIMIT 5000
```

![image](https://github.com/user-attachments/assets/3a7f80a0-81c4-463d-ac31-3c7e2de2235c)

```

### File: requirements.txt
```txt
annotated-types==0.7.0
certifi==2024.12.14
charset-normalizer==3.4.1
idna==3.10
neo4j==5.27.0
neo4j-rust-ext==5.27.0.0
neo4j-uploader==0.6.0
pydantic==2.10.4
pydantic_core==2.27.2
pytz==2024.2
requests==2.32.3
typing_extensions==4.12.2
urllib3==2.3.0

```

### File: clean.py
```py
from neo4j import GraphDatabase
from pprint import pprint 
import json
from config import neo4j_config 

uri = neo4j_config["uri"] 
username = neo4j_config["username"] 
password = neo4j_config["password"] 

driver = GraphDatabase.driver(uri, auth=(username, password))


def clean(tx):
    query = """
    MATCH (n)
	DETACH DELETE n;
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results


try:
	with driver.session() as session:
		results = session.execute_write(clean)
except:
	print("[!] Error deleting the Neo4j DB")
  
```

### File: config.py
```py
neo4j_config = {
    "uri": "bolt://127.0.0.1",
    "username": "neo4j",
    "password": "<password>"
}
```

### File: parse.py
```py
import requests
import json
import re
import os
import sys
from pprint import pp

json_content = ""
directory = 'samples'


## Extract paths + their description + parameters + requestBody + responses 
# print each of them
# create a prompt that asks chatgpt if it does what it says


neo4j_data = {}
neo4j_data["nodes"] = []
neo4j_data["relationships"] = []
path_supported_verbs = ["get", "put", "post", "delete", "options", "head", "patch", "trace"]

# Define Nodes
path_node = {}
verb_node = {}
parameter_node = {}
requestbody_node = {}
response_node = {}
object_node = {}
field_node = {}
security_node = {}

# Define Relationships
object_field_relationship = {}
field_object_relationship = {}
path_verb_relationship = {}
verb_parameter_relationship = {}
verb_requestbody_relationship = {}
verb_response_relationship = {}
requestbody_object_relationship = {}
requestbody_field_relationship = {}
response_object_relationship = {}
response_field_relationship = {}
parameters_relationship = {}
parameters_object_relationship = {}
verb_security_relationship = {}



# Paths
path_node["labels"] = ["Path"]
path_node["key"] = "uid"
path_node["records"] = []

# Verbs
verb_node["labels"] = ["Verb"]
verb_node["key"] = "uid"
verb_node["records"] = []

# Parameters
parameter_node["labels"] = ["Parameter"]
parameter_node["key"] = "uid"
parameter_node["records"] = []

# RequestBody
requestbody_node["labels"] = ["RequestBody"]
requestbody_node["key"] = "uid"
requestbody_node["records"] = []

# Response
response_node["labels"] = ["Response"]
response_node["key"] = "uid"
response_node["records"] = []

# Objects
object_node["labels"] = ["Object"]
object_node["key"] = "uid"
object_node["records"] = []

# Fields
field_node["labels"] = ["Field"]
field_node["key"] = "uid"
field_node["records"] = []

# Security Scheme 
security_node["labels"] = ["Security"]
security_node["key"] = "uid"
security_node["records"] = []

# Add nodes to Neo4J
neo4j_data["nodes"].append(path_node)
neo4j_data["nodes"].append(verb_node)
neo4j_data["nodes"].append(parameter_node)
neo4j_data["nodes"].append(requestbody_node)
neo4j_data["nodes"].append(response_node)
neo4j_data["nodes"].append(object_node)
neo4j_data["nodes"].append(field_node)
neo4j_data["nodes"].append(security_node)

# Add relationships to Neo4J
neo4j_data["relationships"].append(object_field_relationship)
neo4j_data["relationships"].append(field_object_relationship)
neo4j_data["relationships"].append(path_verb_relationship)
neo4j_data["relationships"].append(verb_parameter_relationship)
neo4j_data["relationships"].append(verb_requestbody_relationship)
neo4j_data["relationships"].append(verb_response_relationship)
neo4j_data["relationships"].append(requestbody_object_relationship)
neo4j_data["relationships"].append(response_object_relationship)
neo4j_data["relationships"].append(parameters_relationship)
neo4j_data["relationships"].append(parameters_object_relationship)
neo4j_data["relationships"].append(verb_security_relationship)
neo4j_data["relationships"].append(response_field_relationship)
neo4j_data["relationships"].append(requestbody_field_relationship)






# Object -> Field (object has field)
object_field_relationship["type"] = "has"
object_field_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Object"}
object_field_relationship["to_node"] = { "record_key":"_to_uid", "node_key":"uid", "node_label": "Field" }
object_field_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
object_field_relationship["records"] = []

# Field -> Object (field is of type object)
field_object_relationship["type"] = "is a"
field_object_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Field"}
field_object_relationship["to_node"] = { "record_key":"_to_uid", "node_key":"uid", "node_label": "Object" }
field_object_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
field_object_relationship["records"] = []

# Path -> Verb (field is of type object)
path_verb_relationship["type"] = "can"
path_verb_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Path"}
path_verb_relationship["to_node"] = { "record_key":"_to_uid", "node_key":"uid", "node_label": "Verb" }
path_verb_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
path_verb_relationship["records"] = []

# Verb -> "Parameters", "RequestBody" or "Response"
verb_parameter_relationship["type"] = "contains"
verb_parameter_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Verb"}
verb_parameter_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Parameter" }
verb_parameter_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
verb_parameter_relationship["records"] = []

# Verb -> "RequestBody"
verb_requestbody_relationship["type"] = "sends"
verb_requestbody_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Verb"}
verb_requestbody_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "RequestBody" }
verb_requestbody_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
verb_requestbody_relationship["records"] = []

# Verb ->  "Response"
verb_response_relationship["type"] = "receives"
verb_response_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Verb"}
verb_response_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Response" }
verb_response_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
verb_response_relationship["records"] = []


# "RequestBody" -> Object
requestbody_object_relationship["type"] = "contains a"
requestbody_object_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"RequestBody"}
requestbody_object_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Object" }
requestbody_object_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
requestbody_object_relationship["records"] = []

# "RequestBody" -> Field
requestbody_field_relationship["type"] = "contains a"
requestbody_field_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"RequestBody"}
requestbody_field_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Field" }
requestbody_field_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
requestbody_field_relationship["records"] = []


# "Response" -> Object
response_object_relationship["type"] = "returns a"
response_object_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Response"}
response_object_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Object" }
response_object_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
response_object_relationship["records"] = []

# "Response" -> Field
response_field_relationship["type"] = "returns a"
response_field_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Response"}
response_field_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Field" }
response_field_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
response_field_relationship["records"] = []

# Parameters relationships
parameters_relationship["type"] = "has param"
parameters_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Parameter"}
parameters_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Parameter" }
parameters_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
parameters_relationship["records"] = []

# Parameters -> objects
parameters_object_relationship["type"] = "has object"
parameters_object_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Parameter"}
parameters_object_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Object" }
parameters_object_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
parameters_object_relationship["records"] = []

# Verb -> security relationship
verb_security_relationship["type"] = "secured by"
verb_security_relationship["from_node"] = {"record_key":"_from_uid","node_key":"uid","node_label":"Verb"}
verb_security_relationship["to_node"] = {"record_key":"_to_uid", "node_key":"uid", "node_label": "Security" }
verb_security_relationship["exclude_keys"] = ["_from_uid", "_to_uid"]
verb_security_relationship["records"] = []



if True:
	openapi_file = sys.argv[1] 


	print("============")
	print("OPEN API SPEC DOC: "+ openapi_file)
	with open(openapi_file, "r", encoding="utf-8-sig") as my_file:
		if True:
			json_content = json.load(my_file)
			schemas = {}
			requestBodies = {}
			paths = {}
			securitySchemes = {}
			globalSecurity = {}
			optionalGSec = False
			GSecType = "non-oauth2"
			#popualte global security
			if "security" in json_content:
				globalSecurity = json_content["security"]
				print("****** GLOBAL SECURITY ******")
				for gsec in globalSecurity:
					if not gsec:
						optionalGSec = True
				for gsec in globalSecurity:
					if not gsec:
						continue
					#create globalsec objects (?)
					key = list(gsec.keys())[0]
					value = list(gsec.values())[0]
					security_record = {}
					security_record["uid"] = "global_security" 
					security_record["type"] = "security"
					security_record["name"] = key
					security_node["records"].append(security_record)
					if optionalGSec:
						print("Auth is optional")
					if value == []:
						GSecType = "non-oauth2"
					else:
						GSecType = "oauth2"
			#populate paths and components
			if "components" in json_content:
				if "schemas" in json_content["components"]:
					schemas = json_content["components"]["schemas"]
				if "securitySchemes" in json_content["components"]:
					securitySchemes = json_content["components"]["securitySchemes"]
				if "requestBodies" in json_content["components"]:
					requestBodies = json_content["components"]["requestBodies"]
			#create security schemas objects
			for securitySchema in securitySchemes:
				security_record = {}
				security_record["uid"] = "security_" + securitySchema
				security_record["type"] = "security"
				security_record["name"] = securitySchema
				security_node["records"].append(security_record)
			if "paths" in json_content:
				paths = json_content["paths"]
			for path in paths:
				path_record = {}
				path_record["uid"] = "path_" + path
				path_record["type"] = "path"
				path_record["name"] = path
				path_node["records"].append(path_record)
				if paths[path] is None:
					continue
				for path_verb in paths[path]:
					if path_verb not in path_supported_verbs:
						continue
					print("--------")
					print(path_verb + " " + path)
					#pp(paths[path][path_verb], depth=5, indent=4)
					verb_record = {}
					verb_record["uid"] = path_verb + "_" + path
					verb_record["type"] = "verb"
					verb_record["name"] = path_verb
					verb_node["records"].append(verb_record)
					#link paths with verbs
					relationship = {}
					relationship["_from_uid"] = path_record["uid"]
					relationship["_to_uid"] = verb_record["uid"]
					path_verb_relationship["records"].append(relationship)
					## there are 4 things to be extracted from paths: request, response, parameters and security schema
					if paths[path][path_verb] is None:
						continue
					if "parameters" in paths[path][path_verb]:
						parameters_record = {}
						parameters_record["uid"] = path_verb + "_" + path + "_parameters"
						parameters_record["type"] = "parameters"
						parameters_record["name"] = "params"
						parameter_node["records"].append(parameters_record)
						#link "Parameters" with the verb
						relationship = {}
						relationship["_from_uid"] = verb_record["uid"]
						relationship["_to_uid"] = parameters_record["uid"]
						verb_parameter_relationship["records"].append(relationship)
						for parameter in paths[path][path_verb]["parameters"]:
							if "type" in parameter:
								type_t = parameter["type"]
								parameter_record = {}
								parameter_record["uid"] = path_verb + "_" + path + "_parameter_" + type_t + "_" + parameter["name"]
								parameter_record["name"] =  type_t + "_" + parameter["name"]
								parameter_record["type"] = "parameter"
								parameter_node["records"].append(parameter_record)
								#print(parameter_record)
								# Create link between "Parameters" and the parameter object
								relationship = {}
								relationship["_from_uid"] = parameters_record["uid"]
								relationship["_to_uid"] = parameter_record["uid"]
								parameters_relationship["records"].append(relationship)
							elif "schema" in parameter:
								if "type" in parameter["schema"]:
									type_t = parameter["schema"]["type"]
									parameter_record = {}
									parameter_record["uid"] = path_verb + "_" + path + "_parameter_" + type_t + "_" + parameter["name"]
									parameter_record["name"] =  type_t + " " + parameter["name"]
									parameter_record["type"] = "parameter"
									#print(parameter_record)
									parameter_node["records"].append(parameter_record)
									# Create link between "Parameters" and the parameter object
									relationship = {}
									relationship["_from_uid"] = parameters_record["uid"]
									relationship["_to_uid"] = parameter_record["uid"]
									parameters_relationship["records"].append(relationship)
								elif "$ref" in parameter["schema"]:
									print("TODO: object as parameter")
									reference = parameter["schema"]["$ref"].split("/")
									ref = reference[len(reference) - 1]
									#Link object to params
									relationship = {}
									relationship["_from_uid"] = parameters_record["uid"]
									relationship["_to_uid"] = ref + "_object"
									print(relationship["_from_uid"] + " -> " + relationship["_to_uid"])
									parameters_object_relationship["records"].append(relationship)
									print(ref)
								else:
									print("WTF?")
							else:
								print("Can't find the type of parameter")
					## extract type of response
					if "responses" in paths[path][path_verb]:
						#print("response exists")
						responses_record = {}
						responses_record["uid"] = path_verb + "_" + path + "_responses"
						responses_record["name"] = "responses"
						responses_record["type"] = "responses"
						response_node["records"].append(responses_record)
						#link "responses" with the verb
						relationship = {}
						relationship["_from_uid"] = verb_record["uid"]
						relationship["_to_uid"] = responses_record["uid"]
						verb_response_relationship["records"].append(relationship)
						for response in paths[path][path_verb]["responses"]:
							#print("response: " + response)
							if "content" in paths[path][path_verb]["responses"][response]:
								for c in paths[path][path_verb]["responses"][response]["content"]:
									cnt = paths[path][path_verb]["responses"][response]["content"][c]
					
... [TRUNCATED]
```

### File: scan.py
```py
from neo4j import GraphDatabase
from pprint import pprint 
import json
from config import neo4j_config 

uri = neo4j_config["uri"] 
username = neo4j_config["username"] 
password = neo4j_config["password"] 
driver = GraphDatabase.driver(uri, auth=(username, password))



def get_paths_with_response(tx, _leaf_name):
    query = """
        MATCH p = (start {type: "path"})-[*]->(mid {type: "responses"})-[*]->(end {name: $_leaf_name})
        RETURN p
    """
    result = tx.run(query, _leaf_name=_leaf_name)
    results = [record for record in result.data()]
    return results

def get_parameters(tx, _verb_uid):
    query = """
        MATCH p=(startNode {uid: $_verb_uid})-[*]->(connectedNode)
        WHERE NONE(n IN nodes(p) WHERE n.type IN ['responses', 'security']) 
        WITH last(nodes(p)) AS leafNode
        WHERE NOT (leafNode)-[]->()
        RETURN leafNode
    """
    result = tx.run(query, _verb_uid=_verb_uid)
    results = [record for record in result.data()]
    return results

# returns public readble fields below a given node
def get_read_fields(tx, _obj_uid):
    query = """ 
        MATCH p=(startNode {uid: $_obj_uid})-[*]->(connectedNode)
        WHERE NONE(n IN nodes(p) WHERE n.type IN ['parameters', 'security', 'body']) 
        WITH last(nodes(p)) AS leafNode
        WHERE NOT (leafNode)-[]->()
        RETURN leafNode
    """
    result = tx.run(query, _obj_uid=_obj_uid)
    results = [record for record in result.data()]
    return results

def find_unauthenticated_endpoints(tx):
    query = """
    MATCH (v {type: "verb"})<-[]-(incoming) 
    WHERE NOT EXISTS {
        MATCH (v)-[]->(s {type: "security"})
    }
    RETURN v, incoming
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results

def find_authenticated_endpoints(tx):
    query = """
    MATCH (v {type: "verb"})<-[]-(incoming) 
    WHERE EXISTS {
        MATCH (v)-[]->(s {type: "security"})
    }
    RETURN v, incoming
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results

def find_security_nodes(tx, _obj_uid):
    query = """
    MATCH (n {uid: $_obj_uid})-->(m)
    WHERE m.type = 'security'
    RETURN m
    """
    result = tx.run(query, _obj_uid=_obj_uid)
    results = [record for record in result.data()]
    return results

def check_security(tx):
    query = """
    MATCH (n)
    WHERE n.type = 'security'
    RETURN n
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results


def find_paths(tx, _obj_uid):
    query = """
    MATCH (start), (end {uid: $_obj_uid})
	WHERE start.uid STARTS WITH "path_"
	MATCH path = (start)-[*..10]->(end)
	RETURN path
    """
    result = tx.run(query, _obj_uid=_obj_uid)
    results = [record for record in result.data()]
    return results

def find_objects(tx):
    query = """
    MATCH (n:Object) RETURN n
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results

def find_verb_objects(tx):
    query = """
    MATCH (n)
    WHERE n.type = "verb"
    RETURN n
    """
    result = tx.run(query)
    results = [record for record in result.data()]
    return results



with driver.session() as session:
    print("")
    print("[+] Stats:")
    print("")
    
    objects = session.execute_read(find_verb_objects)
    print("There are " + str(len(objects)) + " unique endpoints" )
    public_endpoints = session.execute_read(find_unauthenticated_endpoints)
    print(" - " + str(len(public_endpoints)) + " public endpoints" )
    protected_endpoints = session.execute_read(find_authenticated_endpoints)
    print(" - " + str(len(protected_endpoints)) + " protected endpoints" )


#might be worth considering to search only by parameter name in the responses, instead of including also the parameter type
# i.e: "username" instead of "string username"

with driver.session() as session:
    print("")
    print("[+] IDOR ID Finder:")
    print("")

    verbs = session.execute_read(find_verb_objects)
    for verb in verbs:
        parameters = session.execute_read(get_parameters, verb['n']['uid'])
        if parameters is not None:
            for parameter in parameters:
                connections = session.execute_read(get_paths_with_response, parameter['leafNode']['name'])
                if connections is not None:
                    print("")
                    print("[*] " + verb['n']['uid'])
                    print(parameter['leafNode']['name'])
                    for connection in connections:
                        path_name = ""
                        verb_name = ""
                        for p in connection["p"]:
                            if type(p) is dict:
                                if p["type"] == "path":
                                    path_name = p["name"]
                                if p["type"] == "verb":
                                    verb_name = p["name"]
                        print(" -> " + verb_name + " " + path_name)

            print("")



with driver.session() as session:
    print(" ")
    print("[+] List objects accessible through public & private endpoints")
    print(" ")
    public_endpoints = session.execute_read(find_unauthenticated_endpoints)
    protected_endpoints = session.execute_read(find_authenticated_endpoints)
    objects = session.execute_read(find_objects)
    public = []
    protected = []
    
    try:
        #print("[+] Public endpoints")
        for endpoint in public_endpoints:
            #print(endpoint['v']['name'] + " " + endpoint['incoming']['name'])
            public.append(endpoint['v']['name'] + " " + endpoint['incoming']['name'])
        #print("[+] Protected endpoints")
        for endpoint in protected_endpoints:
            #print(endpoint['v']['name'] + " " + endpoint['incoming']['name'])
            protected.append(endpoint['v']['name'] + " " + endpoint['incoming']['name'])
        for _object in objects:
            access = []
            connections = session.execute_read(find_paths, _object["n"]["uid"])
            for connection in connections:
                path = ""
                verb = ""
                for p in connection["path"]:
                    if type(p) is dict:
                        if p["type"] == "path":
                            path = p["name"]
                        if p["type"] == "verb":
                            verb = p["name"]
                access.append(verb + " " + path)
            #print(access)
            public_acc = []
            protected_acc = []
            for acc in access:
                if acc in public:
                    public_acc.append(acc)
                if acc in protected:
                    protected_acc.append(acc)
            if len(public_acc) > 0 and len(protected_acc) > 0:
                print(" ")
                print("[+] " + _object["n"]["name"])
                [print("Public: " + item) for item in public_acc]
                [print("Protected: " +item) for item in protected_acc]

    except:
        print("[!] Error listing objects accessible through public & private endpoints!")


    #### List public endpoints ####
    print("")
    print("[+] List public endpoints")
    print("")
    try:
        objects = session.execute_read(find_unauthenticated_endpoints)
        for _object in objects:
            print(_object['v']['name'] + " " + _object['incoming']['name'])
    except:
        print("[!] Error to list public endpoints")


    #### List public fields ####
    print("")
    print("[+] List public readble fields")
    print("")
    
    objects = session.execute_read(find_unauthenticated_endpoints)
    for _object in objects:
        paths = session.execute_read(get_read_fields, _object['v']['uid'])
        print("----")
        print(_object['v']['name'].upper() + " " + _object['incoming']['name'])
        for path in paths:
            print("[-] " + path['leafNode']['name'])


    print("")
    print("[+] IDOR Finder")
    print("")


```

### File: soapi.py
```py
import os
import requests
import json
import re

banner = """
███████╗ ██████╗  █████╗ ██████╗ ██╗
██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║
███████╗██║   ██║███████║██████╔╝██║
╚════██║██║   ██║██╔══██║██╔═══╝ ██║
███████║╚██████╔╝██║  ██║██║     ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
                                    
"""
print(banner)

openapi_files = "samples" 

os.makedirs(openapi_files, exist_ok=True)
os.makedirs("neo4j", exist_ok=True)

if not os.listdir(openapi_files):
	print("[!] The '" + openapi_files + "' directory is empty! Drop the OpenAPI documentations inside it to start the scanner")

for filename in os.scandir(openapi_files):
	if filename.is_file():
		print("[------------------------------]")
		print("[+] Cleaning Neo4j DB..")
		os.system('python3 clean.py ' + filename.path)
		print("[+] Neo4j DB deleted!")

		print("[+] Analyzing " + filename.path)
		os.system('python3 parse.py ' + filename.path + ' >nul 2>&1')
		print("[+] Parsing complete!")

		print("[+] Uploading data to Neo4j server..")
		os.system('python3 upload.py')
		print("[+] Data uploaded succesfully!")

		print("[+] Checking vulnerable paths..")
		os.system('python3 scan.py')
		print("[+] Check complete!")
```

### File: upload.py
```py
from neo4j_uploader import batch_upload
import json
import re
import os
from config import neo4j_config 

config = {
    "neo4j_uri": neo4j_config["uri"],
    "neo4j_user": neo4j_config["username"],
    "neo4j_password": neo4j_config["password"]
}

data = ""

try:
	with open("neo4j/my_neo4j.json", encoding="utf8") as my_file:
	    data = json.load(my_file)

	result = batch_upload(config, data)
except:
	print("[!] Error uploading data to Neo4j server")
```

