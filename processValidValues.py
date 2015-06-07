#!/usr/bin/env python
from bs4 import BeautifulSoup

#  Constants
VALID_VALUES = "Valid Values:"

#  Methods
def processValidValues(soup, swagger):
  
  if (soup.ul == None) : # no attached <ul>
#    swagger['description'] = "{} : {}".format(VALID_VALUES, ' '.join(soup.stripped_strings).replace(VALID_VALUES, '').strip())
    swagger['description'] = "{}".format(' '.join(soup.stripped_strings).replace(VALID_VALUES, '').strip())
    return

  # collect up the array contents
  aryVvals = []
  idx = 0  
  for vval in soup.ul.contents :
    if type(vval) == type(soup.ul) :
      aryVvals.append(vval.code.span.string)
    idx = idx + 1
    
  # join the array contents as csv with or between penultimate and final elements
  vvals = ' or'.join(', '.join(aryVvals).rsplit(',', 1))
  
  # get rid of the <ul> altogether
  soup.ul.extract()
  
  # strip down to string data and get rid of the section title
  main_clause = ' '.join(soup.stripped_strings).replace(VALID_VALUES, '').strip()
#  swagger['description'] = "{} : {} {}".format(VALID_VALUES, main_clause, vvals)
  swagger['description'] = "{} {}".format(main_clause, vvals)
  return
  


#  -   -   -   -   -   -   -   -   -   -   -   
#  Main routine (for testing)
def main():
  
  from test.testdataValidValues import test_values
  from test.testdataValidValues import swagger
  
  idx = 0
  for frag in test_values :
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    soup = BeautifulSoup(frag)
#    if idx == 2 :
    if idx != -1 :
      processValidValues(soup.body.li, swagger)
      print(swagger)
    idx = idx + 1
    
  print(">>~~~~~~~~~~~~~~~~~~~~~~~~~<<")


if __name__ == "__main__": main()

