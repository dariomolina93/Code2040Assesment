#Module that will allow us to create our json dictionary.
import json
#Module that will allow us to connect to the API.
import requests

"""
Name: Dario Molina
8/30/16
Description: Connect to Code2040 API, receive a string, reverse the string then send the reversed string back through a request for verification.
"""

#URL where we obtain and send information to the API
retrieve_info_url = "http://challenge.code2040.org/api/reverse"
send_info_url = "http://challenge.code2040.org/api/reverse/validate"

#Our API token
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#Creating a dictionary where it contains our access token, that will allow us to connect to the API
retrieve_info_dictionary ={"token":accessKey}

#Obtaining the information from the API and storing it in variable r
r = requests.post(retrieve_info_url, json = retrieve_info_dictionary)

#Printing the string that it is stored in r
print r.text

#Using the "extended slice operator", it reverses the string and stores it in our new variable "reversedWord" 
reversedWord = r.text[::-1]

#dictionary where we will store our reversedWord, so we can send back to the API for verification.
send_info_dictionary = {"token": accessKey, "string": reversedWord}


#sending request to API for verification that we passed this challenge.
t = requests.post(send_info_url, json = send_info_dictionary)

#printing contents of our t request
print t.text
print t.status_code

