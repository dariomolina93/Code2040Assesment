import json
import requests

"""
Name: Dario Molina
Date: 9/3/16
Description: Write a program that connects to Code2040's API, retrieve a dictionary with keys 'needle' and 'haystack'. Needle is a string, and haystack in an array of strings.  Locate the needle in the haystack array, and send back the position or 'index' through a request to Code2040's API.
"""

#URL where we obtain and send information to API
retrieve_info_url = "http://challenge.code2040.org/api/haystack"
send_info_url = "http://challenge.code2040.org/api/haystack/validate"

#token to connect to the API
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#dictionary that will store our API token
retrieve_info_dictionary ={"token": accessKey}

#sending the request and obtaining the information from the API
r = requests.post(retrieve_info_url, json = retrieve_info_dictionary)


inputDic = json.loads(r.text)#convert our string into a dictionary 

array = inputDic["haystack"]#obtaining array from inputDic and storing it in "array"
word = inputDic["needle"]#obtaining the word we will be looking for and storing it in "word"

#Finding the index of where the needle is stored
index = array.index(word)


#dictionary that will store our accessKey and index of where the needle was stored in the haystack array.
send_info_dictionary = {"token": accessKey,"needle":index}

#sending the request to validate the challenge
t = requests.post(send_info_url, json = send_info_dictionary)

#printing the contents of our request that were stored in t
print t.text
