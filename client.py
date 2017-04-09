#!/usr/bin/env python
import requests
import time
# arguments: server, file
# 
server="http://localhost:5000/add"
path="/root/.bash_history"
for line in open(path):
  print line.strip("\n")
  payload={ "data": line.strip("\n") }
  r = requests.post(server,payload)
  print r.text
  time.sleep(0.01) 
   

#open file for reading

#create payload
#r = requests.post( server, payload )

