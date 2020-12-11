# importing required libraries
import json
from urllib.request import urlopen
name=input("Please Enter your Name : ")
# create an free account in www.gender-api.com
# account activation will take some time...
# after activation get the authentication key and use it in mykey
mykey="paste your key here" 
#url to open and get the response
url="https://gender-api.com/get?name="
#concatinating the name you entered and your api key..
try:
   url=url+f"{name}&key={mykey}"
#opening the final url...
   respose=urlopen(url)
#decoding the data to json format
   decode=respose.read().decode("utf-8")
   data=json.loads(decode)
# printing the gender of the name you entered...
   print("Gender : "+data["gender"])
except(Exception):
    print("please enter the valid name..")

