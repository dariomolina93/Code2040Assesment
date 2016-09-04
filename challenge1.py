import json
import requests

"""
Name: Dario Molina
8/27/16
Description: Write a program that successfully connects to the registration endpoint of Code2040's API.
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
