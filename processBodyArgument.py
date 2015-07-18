#!/usr/bin/env python
from bs4 import BeautifulSoup
from processValidValues import processValidValues
from processDefaults import processDefaults
from processModelName import determineModelName
from pprint import pprint
import json
import re

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"
NONE = -1

def processBodyArgument(soup, swggr, cursor):

  # if cursor['entity'] == "board" and cursor['method'] != "get" \
  # and cursor['path'] in ["/boards","/cards","/checklists","/labels","/lists","/organizations","/sessions","/webhooks"] :
  # # ["/boards/{idBoard}/lists"] :

  if cursor['path'] in ["xxxxx/members/{idMember}/boardStars/{idBoardStar}/idBoard"] :
    debugPrint = True
  else :
    debugPrint = False


  name = soup.code.span.text
  if debugPrint : print 'Name : {}\n\n'.format(name)

  required = False
  if REQUIRED in soup.code.span.next_element.next_element.strip() :
    required = True

  swagger = swggr['paths'][cursor['path']][cursor['method']]


  '''
  print "##### "
  print repr(soup.code.span.next_element.next_element.strip())
  print "##### "
  '''

  parameter = {
      "name" : name.strip()
    , "required" : required
    , "in" : "query"
    , "type" : "string"
    , "description" : "undefined"
    , "default" : "undefined"
  }
  vvals = soup.find_all(text='Valid Values:')

  '''
  print "::::: "
  print ' {}'.format(vvals)
  print "::::: "
  '''
  for vval in vvals :
    processValidValues(vval.parent.parent, parameter)

  defaults = soup.find_all(text='Default:')
  for default in defaults :
    processDefaults(default.parent.parent, parameter)

  model = determineModelName(cursor['path'])

  if model not in swggr['definitions']:
    swggr['definitions'][model] = {
      "type" : "object",
      "properties" : {
      },
      "xml":{
        "name":cursor['entity']
      }
    }

  swggr['definitions'][model]['properties'][parameter['name']] = {
    'type' : parameter['type'],
    'description' : parameter['description'],
  }

  if debugPrint :
    print 'Swagger definitions : {}\n\n'.format(model)
    pprint(swggr['definitions'][model])

#  swagger["parameters"].append(parameter)

  return model


#  -   -   -   -   -   -   -   -   -   -   -
#  Main routine (for testing)
def main():

  from test.testdataBodyArgument import test_values
  from test.testdataBodyArgument import swagger
  from test.testdataBodyArgument import cursor

  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 0 :
    if idx != -1 :
      processBodyArgument(soup.body, swagger, cursor)
    idx = idx + 1

  print json.dumps(swagger)


  print("\n>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<\n")



if __name__ == "__main__": main()

'''
  "List":{
    "type":"object",
    "properties":{
      "name":{
        "type":"string"
      },
      "pos":{
        "type":"string",
        "default":"top"
      }
    },
    "xml":{
      "name":"Pet"
    }
  }

'''
