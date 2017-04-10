#!/usr/bin/env python
import requests
import time

import argparse
parse = argparse.ArgumentParser(description="Connect to Bash History server")
parse.add_argument("--server", "-s", dest="server", default="http://localhost:5000")
parse.add_argument("--file" ,  "-f", dest="file", help="Sample file for updating server")
parse.add_argument("--debug",  "-d", dest="debug", action='store_true', default=False)
parse.add_argument("--update",  "-u", dest="update", action="store_true", default=False,
                    help="Request a model update")
parse.add_argument("--predict", "-p", dest="query")
args = parse.parse_args()
if args.debug:
  print args



if args.file:
   print "Uploading %s" % args.file
   for line in open(args.file):
      if args.debug:
   		print line.strip("\n")
      payload={ "data": line.strip("\n") }
      r = requests.post(args.server + "/add", payload )
      print r.text
      time.sleep(0.01) 
 	
if args.update:
  r = requests.get( args.server + "/update" )
  print r.text

if args.query:
  payload={ "q": args.query }
  r = requests.get( args.server + "/getdebug", params=payload )
  r = requests.get( args.server + "/predict", params=payload )
  print r.text

