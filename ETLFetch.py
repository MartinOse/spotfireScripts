from System import DateTime
from os import system

def curlPull(id):
	ds_id = str(id)
	data = "start="+startDate+"T13:00:00Z&end="+endDate+"T13:30:00Z&force=false"
	endpoint = "https://organization.datatap.adverity.com/api/datastreams/"+ds_id+"/fetch_fixed/"
	system('curl -H "Authorization: Token '+auth+'" '+endpoint+' --data '+data+'')

startDate = DateTime.Today.ToString("yyyy-MM-dd")
endDate = DateTime.Today.ToString("yyyy-MM-dd")

ds_list = [446]
auth = "yourAPIkeyhere"


for el in ds_list:
	curlPull(el)