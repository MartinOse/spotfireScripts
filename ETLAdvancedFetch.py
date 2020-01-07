from System import DateTime
from os import system
import subprocess
import re
import time
from Spotfire.Dxp.Data import *
from Spotfire.Dxp.Data.Import import *


def verifyFetch(id):
	ds_id = str(id)
	# Using the subprocess module to send a curl request
	cmd = 'curl -H "Authorization: Token '+auth+'" https://organization.datatap.adverity.com/api/datastreams/'+ds_id+'/'
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	out = proc.communicate()
	el = out[0]

	# Regex extract API information from curl return, to get last_fetch timestamp
	txt = re.findall('"last_fetch":"\d+-\d+-\d+\w\d+:\d+:\d+\w"', str(el))
	txt = str(txt)
	txt = re.findall('\d+-\d+-\d+\w\d+:\d+:\d+\w', txt)
	return txt
	
def curlFetch(id):
	ds_id = str(id)
	data = "start="+startDate+"T00:00:00Z&end="+endDate+"T23:00:00Z&force=false"
	endpoint = "https://organization.datatap.adverity.com/api/datastreams/"+ds_id+"/fetch_fixed/"
	system('curl -H "Authorization: Token '+auth+'" '+endpoint+' --data '+data+'')

def tableRefresh():
	for t in Document.Data.Tables:
		if t.IsRefreshable:
			t.Refresh()

startDate = DateTime.Today.ToString("yyyy-MM-dd")
endDate = DateTime.Today.ToString("yyyy-MM-dd")

ds_arr = [424, 423]
pre_arr = []

auth = "yourAuthKeyHere"


for id in ds_arr:
	pre_arr.append(verifyFetch(id))
	curlFetch(id)

i = 0
for id in ds_arr:
	while(pre_arr[i]==verifyFetch(id)):
		time.sleep(3)
		if(pre_arr[i]!=verifyFetch(id)):
			time.sleep(3)
			tableRefresh()
			break
	i += 1