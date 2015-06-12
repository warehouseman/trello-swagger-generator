#!/usr/bin/env python
from bs4 import BeautifulSoup
from processArgument import processArgument
import json
import sys

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"


#  Methods
def processArguments(soup, swagger, path_fields):

  '''
  print ' ..... ..... ..... ..... ..... ..... ..... '
  print soup.ul.contents
  print ' ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ '
  sys.exit()
  '''
  
  arguments = soup.ul.contents

  idx = 0
  for argument in arguments :   # process all the fields that follow the "?" in the URL
    if isinstance(argument, type(soup.li)) :
#      print "#{} -- {}".format(idx, argument)
      processArgument(argument, swagger)
      idx = idx + 1
    
  for field in path_fields :   # process all the fields that form part of the URL
#    print "------------ new parameter -- {}".format(field)
    swagger["parameters"].append({
        "name" : field.iterkeys().next()
      , "required" : "true"
      , "in" : "path"
      , "type" : "string"
      , "description" : field.itervalues().next()
      , "default" : "undefined"
    })

  #  add the authorization key field
    swagger["parameters"].append({
        "name" : "key"
      , "required" : "true"
      , "in" : "query"
      , "type" : "string"
      , "description" : '<a href="https://trello.com/1/appKey/generate"  target="_blank">Generate your application key</a>'
      , "default" : "undefined"
    })

  #  add the 3rd party token field field
    swagger["parameters"].append({
        "name" : "token"
      , "required" : "true"
      , "in" : "query"
      , "type" : "string"
      , "description" : '<a href="https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user"  target="_blank">Getting a token from a user</a>'
      , "default" : "undefined"
    })

  return
  
#  -   -   -   -   -   -   -   -   -   -   -   
#  Main routine (for testing)
def main():
  
  from test.testdataArguments import test_values
  from test.testdataArguments import swagger
  
  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 1 :
    if idx != -1 :
      processArguments(soup.body.contents[0], swagger)
    idx = idx + 1

  print(">>~~~~~~~~~~~ ? ~~~~~~~~~~~<<")
  print "JSON {}".format(json.dumps(swagger))
  print("<<~~~~~~~~~~~~~~~~~~~~~~~~~>>")


if __name__ == "__main__": main()

