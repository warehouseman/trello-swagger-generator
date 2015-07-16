#!/usr/bin/env python
from bs4 import BeautifulSoup
from processValidValues import processValidValues
from processDefaults import processDefaults
from processModelName import determineModelName
import json

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"
NONE = -1

def processQueryArgument(soup, swggr, cursor):

  swagger = swggr['paths'][cursor['path']][cursor['method']]

  '''
  print "##### "
  print repr(soup.code.span.next_element.next_element.strip())
  print "##### "
  '''

  name = soup.code.span.text
  # print 'Name : {}\n\n'.format(name)

  required = False
  if REQUIRED in soup.code.span.next_element.next_element.strip() :
    required = True


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

  swagger["parameters"].append(parameter)

  return



#  -   -   -   -   -   -   -   -   -   -   -
#  Main routine (for testing)
def main():

  from test.testdataQueryArgument import test_values
  from test.testdataQueryArgument import swagger
  from test.testdataQueryArgument import cursor

  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 0 :
    if idx != -1 :
      processQueryArgument(soup.body, swagger, cursor)
    idx = idx + 1

  print json.dumps(swagger)


  print("\n>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<\n")



if __name__ == "__main__": main()

