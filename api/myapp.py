import requests
import json

URL= "http://127.0.0.1:8000/api/employeeview/"

# Read Data
def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id}
	headers={'content-Type':'application/json'}
	json_data=json.dumps(data)
	r= requests.get(url= URL,headers=headers,data=json_data)
	data=r.json()
	print(data)
get_data()

# Create Data
def post_data():
	data= {
		'name':'Shiva',
		'mob': 7067564356 ,
		'email':'shivanshi@gmail.com',
		'city':'Aurangabad'
		}

	headers={'content-Type':'application/json'}
	json_data=json.dumps(data)
	r=requests.post(url=URL ,headers=headers, data= json_data)
	data=r.json()
	print(data)
# post_data()

# post_data()
# Update Data
def update_data():
	data= {
		'id': 1 ,
		'name':'Heena',
		'email':'heena@gmail.com',
		'city':'Pune'
		}
	headers={'content-Type':'application/json'}
	json_data=json.dumps(data)
	r=requests.put(url=URL , headers = headers ,data= json_data)
	data=r.json()
	print(data)
# update_data()

def delete_data():
	data= {
		'id': 1 
		}
	headers={'content-Type':'application/json'}
	json_data=json.dumps(data)
	r=requests.delete(url=URL,headers=headers, data= json_data)
	data=r.json()
	print(data)
# delete_data()