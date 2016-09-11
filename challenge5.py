import json
import requests
from datetime import * 
import dateutil.parser

"""
Name: Dario Molina
Date: 9/4/16
Description: Make a request to Code2040 API, retrieve a dictionary where one key is "datestamp" with a value that contains a string and it is a date formated in IOS 8601.  The second key is "interval" which is an integer representing seconds.  The goal of the program is to add the the seconds into the date that is in format IOS 8601, and send the new date back to the API for validation.  Make sure the new date we send to the API is in format IOS 8601 as well.
"""
#URl's where we obtain and send information to Code2040's API
retrieve_info_url = "http://challenge.code2040.org/api/dating"
send_info_url = "http://challenge.code2040.org/api/dating/validate"

#token to connect to the API
accessKey = "37bc2120300edb47c357ab11625cbfa7"

#dictionary that will allow us to connect to API
retrieve_dictionary ={"token": accessKey}

#sending the request and obtaining the information from the API
r = requests.post(retrieve_info_url, json = retrieve_dictionary)

#print the contents of retrieved from our request
print r.text

#convert our string retrieved from our request into a dictionary
inputDic = json.loads(r.text)

#storing the values of our dictionary into appropiate variables so we can use to complete our task

date = inputDic['datestamp']#storing the datestamp value into date.  Value is of type string.
interval = inputDic['interval']#storing the amount of seconds into interval. Value is of type int.


#converting our date into a datetime object.  We need to convert it into a datetime object so we are able to add the seconds from our interval.
dateObject = dateutil.parser.parse(date)

#printing our object to make sure converstion is succesful
print dateObject

#adding our time interval into our datetime object to obtain our new date object 
newDateObject = dateObject + timedelta(seconds = interval)

#converting our newDateObject into ISO 8601 format, which transforms it into a string and stores in newDateIOS.
newDateIOS = newDateObject.isoformat()

"""
When we print date, it is a string of type ISO 8601 format such as: 2016-09-T01:03:04Z.
After our conversion when we print out newDateIOS, the format is: 2016-09-13T01:03:09+00:00.
Since the description says we need to send a date in the same format as the one we received from our request, I did a substring from 0-19 from newDateIOS and stored that new string into finalDate. The reason I chose from 0-19, is because we want to store the contents of our newDateIOS, up to but not including the '+'.  So we can then concatenate a 'Z' and finalDate could finally be in the right format that satisfies one of our objectives.

I had though about using a for loop that goes through each index and stores the elements of each index in finalDate up to it reached the index containing the '+'. But I though about the Big-O and using a for loop it would make our program to have O(n), but using a substring it would make our Big-O to be constant O(1) which is better.
"""

#substring that goes from index 0 up to but not including index 19, and storing string into finalDate.
finalDate = newDateIOS[:19]

#concatenating a Z so we could have the right format that our program requires.
finalDate = finalDate + 'Z'

#displaying the contents of finalDate
print finalDate

#dictionary that contains our access key and finalDate which contains the new date with the added time interval formatted in ISO 8601 format.
send_info_dictionary ={'token':accessKey, 'datestamp':finalDate}

#sending the request to validate our challenge
t = requests.post(send_info_url, json = send_info_dictionary)

#printing the contents of our request t
print t.text
