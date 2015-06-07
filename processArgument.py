#!/usr/bin/env python
from bs4 import BeautifulSoup
from processValidValues import processValidValues
from processDefaults import processDefaults
import json

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"

#  Methods
def processArgument(soup, swagger):
  
  '''
  print "##### "
  print repr(soup.code.span.next_element.next_element.strip())
  print "##### "
  '''
  name = soup.code.span.text
#  print name
  required = "false"
  if REQUIRED in soup.code.span.next_element.next_element.strip() :
    required = "true"
    
  
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
  
  from test.testdataArgument import test_values
  from test.testdataArgument import swagger

  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 0 :
    if idx != -1 :
      processArgument(soup.body, swagger)
    idx = idx + 1

  print json.dumps(swagger)    
  print(">>~~~~~~~~~~~~~~~~~~~~~~~~~<<")


if __name__ == "__main__": main()

