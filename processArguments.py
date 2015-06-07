#!/usr/bin/env python
from bs4 import BeautifulSoup
from processArgument import processArgument
import json
import sys

#  Constants
DEFAULT = "Default:"
REQUIRED = "required"


#  Methods
def processArguments(soup, swagger):

  '''
  print ' ..... ..... ..... ..... ..... ..... ..... '
  print soup.ul.contents
  print ' ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ '
  sys.exit()
  '''
  
  arguments = soup.ul.contents

  idx = 0
  for argument in arguments :
    if isinstance(argument, type(soup.li)) :
#      print "#{} -- {}".format(idx, argument)
      processArgument(argument, swagger)
      idx = idx + 1
    
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

