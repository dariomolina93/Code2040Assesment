import json
import requests

"""
Name: Dario Molina
8/27/16
Description: Connect to Code2040 API, receive a string, reverse the string then send the reversed word back through a request to the desired destination.
"""

#URL where we connect to the API
retrieve_info_url = "http://challenge.code2040.org/api/register"

#token to connect to the API
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#Github repository URL
github_url = "https://github.com/dariomolina93/Code2040Assesment"

#Creating a dictionary where it contains our access token, github account, that will allow us to connect to the API
retrieve_info_dictionary ={"token":accessKey, "github": github_url}

#Obtaining the information from the API and storing it in variable r
#The information stored in r will be of type "string".
r = requests.post(retrieve_info_url, json = retrieve_info_dictionary)

#Printing the content of r
print r.text
print r.status_code
