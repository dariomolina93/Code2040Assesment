#module that will allow us to use json format for our dictionaries.
import json
#module that will allow us to connect to the API.
import requests

"""
Name: Dario Molina
Date: 9/3/16
Description: Write a program that connects to Code2040's API. Then, retrive a dictionary with keys prefix and array. 
 Prefix, is a string and array is an array of strings. Your job is to return an array containing
 only the strings that do not start with that prefix. 
Once new array is built, POST a dicitonary back to API and check for verification.
"""
#URl's where we obtain and send information to Code2040's API
retrieve_info_url = "http://challenge.code2040.org/api/prefix"
send_info_url = "http://challenge.code2040.org/api/prefix/validate"

#Our API token
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#dictionary that will allow us to connect to the API
retrieve_dictionary ={"token": accessKey}

#sending the request and obtaining the information from the API
r = requests.post(retrieve_info_url, json = retrieve_dictionary)

#array where we will store our words that do not start with the prefix
noPrefixArray = []

json_dictionary = json.loads(r.text)#making a string into a dictionary and storing in variable "inputDic"

array = json_dictionary["array"]#obtaining the array from the dictionary and storing it in a variable "array"
prefix = json_dictionary["prefix"]#obtaining the string that is associated with prefix and storing it in "prefix'


for word in array:#for loop that goes through each string in our array 

  checkPrefix = word[:len(prefix)]#for each word in our array, we are doing a substring from 0 to the length of prefix and storing in "checkPrefix" so we could check if the word starts with the prefix
  
# if the word does not start with the prefix, we will add it to our noPrefixArray array. 
  if(checkPrefix != prefix):
     noPrefixArray.append(word)


#dictionary that contains our access key and array of strings without the prefix
send_info_dictionary = {"token": accessKey, "array": noPrefixArray}

#sending the request to validate the challenge
t = requests.post(send_info_url, json = send_info_dictionary)

#printing the contents of our request that were stored in t(informing us if we passed or if we did not passed the challenge).
print t.text

