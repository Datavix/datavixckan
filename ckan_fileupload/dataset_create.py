import urllib2
import urllib
import json
import pprint


def package_create(owner_org, name, title, notes):
	# Put the details of the dataset we're going to create into a dict.
	dataset_dict = {
		'owner_org': owner_org,
		'name': name,
		'title': title,
		'notes': notes
	}

	# Use the json module to dump the dictionary to a string for posting.
	data_string = urllib.quote(json.dumps(dataset_dict))

	# We'll use the package_create function to create a new dataset.
	request = urllib2.Request(
	    'http://www.datavix.cn/api/action/package_create')

	# Creating a dataset requires an authorization header.
	# Replace *** with your API key, from your user account on the CKAN site
	# that you're creating the dataset on.
	request.add_header('Authorization', 'a1e832ca-9ded-4539-945e-529705b93141')

	# Make the HTTP request.
	response = urllib2.urlopen(request, data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())
	assert response_dict['success'] is True

	return response_dict['result']['id']

def resource_create(package_id, data_link):
	# Put the details of the dataset we're going to create into a dict.
	dataset_dict = {
		"package_id":package_id,
		"name":"CSV",
		"url":data_link,
		"format":"CSV"
	}

	# Use the json module to dump the dictionary to a string for posting.
	data_string = urllib.quote(json.dumps(dataset_dict))

	# We'll use the package_create function to create a new dataset.
	request = urllib2.Request(
	    'http://www.datavix.cn/api/action/resource_create')

	# Creating a dataset requires an authorization header.
	# Replace *** with your API key, from your user account on the CKAN site
	# that you're creating the dataset on.
	request.add_header('Authorization', 'a1e832ca-9ded-4539-945e-529705b93141')

	# Make the HTTP request.
	response = urllib2.urlopen(request, data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())
	assert response_dict['success'] is True

	return response_dict['result']['id']

fname = 'data_gov_local_government_csv.json'
owner_org = 'us-local-government'
with open (fname) as data_file:
        lines = data_file.readlines()
	index = 1
        for line in lines:
                data = json.loads(line)
		name = data['name'].replace(" ", "").replace("\'", "").replace(",", "").replace(":", "").replace("(", "").replace(")", "").lower()
		#print "name: " + name + "\n"
		try:
                	package_id = package_create(owner_org, name, data['name'], data['notes'])
                	resource_id = resource_create(package_id, data['data_link'])
                	print "Successfully create resource: " + resource_id + ": " + data['name'] + "\n"
		except:
			print "Error Line number: " + str(index) + "\n"
	
		index = index + 1	
