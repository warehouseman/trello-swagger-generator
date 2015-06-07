#!/usr/bin/env python
from bs4 import BeautifulSoup

#  Constants
DEFAULT = "Default:"

#  Methods
def processDefaults(soup, swagger):

  default = ''
  for string in soup.code.stripped_strings :
    default = ' and'.join(', '.join(string.split(',')).rsplit(',', 1))

  swagger['default'] = default
  return
  
  
#  -   -   -   -   -   -   -   -   -   -   -   
#  Main routine (for testing)
def main():
  from test.testdataDefaults import test_values
  from test.testdataDefaults import swagger
  
  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 1 :
    if idx != -1 :
      processDefaults(soup.body.li, swagger)
      print "swagger = {}".format(swagger)
    idx = idx + 1
    
  print(">>~~~~~~~~~~~~~~~~~~~~~~~~~<<")


if __name__ == "__main__": main()

