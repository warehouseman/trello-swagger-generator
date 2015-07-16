#!/usr/bin/env python
import re
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

  print(">>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<\n")


  paths = []
  paths.append('/boards/{idBoard}/prefs/background')
  paths.append('/boards/{idBoard}/prefs/calendarFeedEnabled')
  paths.append('/boards/{idBoard}/prefs/cardAging')
  paths.append('/boards/{idBoard}/prefs/cardCovers')
  paths.append('/boards/{idBoard}/prefs/comments')
  paths.append('/boards/{idBoard}/prefs/invitations')
  paths.append('/boards/{idBoard}/prefs/permissionLevel')
  paths.append('/boards/{idBoard}/prefs/selfJoin')
  paths.append('/boards/{idBoard}/prefs/voting')
  paths.append('/boards/{idBoard}/calendarKey/generate')
  paths.append('/boards/{idBoard}/labelNames/blue')
  paths.append('/boards/{idBoard}/labelNames/green')
  paths.append('/boards/{idBoard}/labelNames/orange')
  paths.append('/boards/{idBoard}/labelNames/purple')
  paths.append('/boards/{idBoard}/labelNames/red')
  paths.append('/boards/{idBoard}/labelNames/yellow')
  paths.append('/boards/{idBoard}/emailKey/generate')
  paths.append('/boards/{idBoard}/myPrefs/emailPosition')
  paths.append('/boards/{idBoard}/myPrefs/idEmailList')
  paths.append('/boards/{idBoard}/myPrefs/showListGuide')
  paths.append('/boards/{idBoard}/myPrefs/showSidebar')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarActivity')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarBoardActions')
  paths.append('/boards/{idBoard}/myPrefs/showSidebarMembers')

  paths.append('/boards/{idBoard}/checklists')
  paths.append('/boards/{idBoard}/labels')
  paths.append('/boards/{idBoard}/lists')
  paths.append('/boards/{idBoard}/closed')
  paths.append('/boards/{idBoard}/desc')
  paths.append('/boards/{idBoard}/idOrganization')
  paths.append('/boards/{idBoard}/members')
  paths.append('/boards/{idBoard}/name')
  paths.append('/boards/{idBoard}/subscribed')

  paths.append('/boards/{idBoard}')

  paths.append('/boards')

  paths.append('/boards/{idBoard}/members/{idMember}')
  paths.append('/boards/{idBoard}/memberships/{idMembership}')


  for path in paths :
    idx = 0
    for pattern in patterns :
      mm = pattern.match(path)
      if mm : print(">>~~~~~ {})   {} ~~~~<<".format(idx, path))
      idx = idx+1

  print("\n>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<\n")



if __name__ == "__main__": main()

