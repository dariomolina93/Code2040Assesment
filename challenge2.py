import json
import requests

"""
Name: Dario Molina
8/30/16
Description: Connect to Code2040 API, receive a string, reverse the string then send the reversed word back through a request to the desired destination.
"""

#URL where we obtain and send information from the API
retrieve_info_url = "http://challenge.code2040.org/api/reverse"
send_info_url = "http://challenge.code2040.org/api/reverse/validate"

#token to connect to the API
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#Github repository URLclear
github_url = "https://github.com/dariomolina93/Code2040Assesment"


#Creating a dictionary where it contains our access token, github account, that will allow us to connect to the API
retrieve_info_dictionary ={"token":accessKey}

#Obtaining the information from the API and storing it in variable r
r = requests.post(retrieve_info_url, json = retrieve_info_dictionary)

#Printing the string that it is stored in r
print r.text

#Using the "extended slice operator", it reverses the string and stores it in our new variable "reversedWord" 
reversedWord = r.text[::-1]

#dictionary where we will store our reversedWord 
send_info_dictionary = {"token": accessKey, "string": reversedWord}


#sending the request to the desired url with the dictitionary in json format.
t = requests.post(send_info_url, json = send_info_dictionary)

#printing status of our t request
print t.text
print t.status_code

