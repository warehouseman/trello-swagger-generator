#!/usr/bin/env python
from bs4 import BeautifulSoup
from processQueryArgument import processQueryArgument
from processBodyArgument import processBodyArgument
import json
import sys
import re

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"


#  Methods
def processArguments(soup, swggr, path_fields, cursor):

  '''
  print ' ..... ..... ..... ..... ..... ..... ..... '
  print soup.ul.contents
  print ' ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ '
  sys.exit()
  '''

  if cursor['path'] in ["/members/{idMember}/boardStars/{idBoardStar}/idBoard"] :
    debugPrint = True
  else :
    debugPrint = False

  if debugPrint :
    print ' ..... ..... ..... ..... ..... ..... ..... '
    print path_fields
    print 'idBoardStar' in path_fields
    print ' ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ '


  swagger = swggr['paths'][cursor['path']][cursor['method']]
  arguments = soup.ul.contents

  processed_args = []

  for field in path_fields :   # process all the fields that form part of the URL
#    print "------------ new parameter -- {}".format(field)
    name_arg = field.iterkeys().next()
    swagger["parameters"].append({
        "name" : name_arg
      , "required" : True
      , "in" : "path"
      , "type" : "string"
      , "description" : field.itervalues().next()
      , "default" : "undefined"
    })
    processed_args.append(name_arg)

  idx = -1
  modelName = None
  action = 'added'
  for argument in arguments :
    if isinstance(argument, type(soup.li)) :
      name_arg = argument.code.span.text
      if name_arg not in processed_args :
  #      idx = idx + 1
  #      print "#{} -- {}".format(idx, argument)
        if cursor['method'] in ["put", "post"] :
          # process all the fields that are sent in the body
          modelName = processBodyArgument(argument, swggr, cursor)
          if cursor['method'] == "put" :
            action = 'updated'
        else :
          # process all the fields that follow the "?" in the URL
          processQueryArgument(argument, swggr, cursor)

  if modelName :
    modelTitle = re.sub(
        "([a-z])([A-Z])","\g<1> \g<2>",
        modelName
      ).replace('_', ' ').title()
    swagger["parameters"].append({
        "name" : "body"
      , "required" : True
      , "in" : "body"
      , "description" : 'Attributes of "' + modelTitle + '" to be ' + action + '.'
      , "schema" : { "$ref" : '#/definitions/' + modelName }
    })

#  add the authorization key field
  swagger["parameters"].append({
      "name" : "key"
    , "required" : True
    , "in" : "query"
    , "type" : "string"
    , "description" : '<a href="https://trello.com/1/appKey/generate"  target="_blank">Generate your application key</a>'
    , "default" : "undefined"
  })

#  add the 3rd party token field field
  swagger["parameters"].append({
      "name" : "token"
    , "required" : True
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
  from test.testdataArguments import cursor
  from test.testdataArguments import pathFields

  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 1 :
    if idx != -1 :
      processArguments(soup.body.contents[0], swagger, pathFields, cursor)
    idx = idx + 1

  print(">>~~~~~~~~~~~ ? ~~~~~~~~~~~<<")
  print "JSON {}".format(json.dumps(swagger))
  print("<<~~~~~~~~~~~~~~~~~~~~~~~~~>>")



if __name__ == "__main__": main()

