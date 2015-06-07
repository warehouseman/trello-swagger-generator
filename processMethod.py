#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from processArguments import processArguments
import json
import sys

#  Constants
REQUIRED_PERMISSIONS="Required permissions:"
NOTES = "Notes:"

#  Methods
def prepareNote(soup) :
  notes_line = soup.next_element
  aryNotes = []
  phrase = ''
  while notes_line != None :
    if NOTES not in notes_line  :
      if isinstance(notes_line, type(soup)) :
        phrase = ''.join(['\'' + ' '.join(notes_line.stripped_strings).strip() + '\''])
        aryNotes.append(phrase)
      else :
        phrase = notes_line.strip()
        aryNotes.append(phrase)
        
    notes_line = notes_line.next_sibling
      
  return ' '.join(aryNotes)

def processMethod(soup, swagger, entity):


  '''  
  print "# {}".format(soup)
  sys.exit()
  '''
  
  namePath = soup.h2.span.text.replace('[', '{').replace(']', '}').strip()
  nameMethod = soup.h2.next_element.lower().strip()
#  print "Method : {}, Path : {}".format(nameMethod, namePath)

  if   namePath not in swagger['paths']           :  swagger['paths'][namePath]             = {}
  if nameMethod not in swagger['paths'][namePath] :  swagger['paths'][namePath][nameMethod] = {"tags" : [entity]}

  soup.h2.extract()

  if NOTES in soup.ul.li.next_element :
    swagger['paths'][namePath][nameMethod]['description'] = prepareNote(soup.ul.li)
#    print swagger['paths'][namePath][nameMethod]['description']
    soup.ul.li.extract()
        
  if REQUIRED_PERMISSIONS in soup.ul.li.next_element :
    permission = ' and'.join(''.join(soup.ul.li.stripped_strings).replace(REQUIRED_PERMISSIONS, '').rsplit(',', 1))
    auth = ["read:boards"]
    if "get" not in nameMethod : auth.append("write:boards")
    swagger['paths'][namePath][nameMethod]['security'] = [ { "trello_auth": auth } ]
#    print swagger['paths'][namePath][nameMethod]['security']
    soup.ul.li.extract()
  
  arguments = soup.ul.li

  '''
  print ' ---- '
  print arguments
  print ' ---- '
  '''
  
  swagger['paths'][namePath][nameMethod]['parameters'] = []
  if arguments.ul != None :
    processArguments(arguments, swagger['paths'][namePath][nameMethod])
      
  return
  


#  -   -   -   -   -   -   -   -   -   -   -   
#  Main routine (for testing)
def main():
  
  from test.testdataMethod import test_values
  from test.testdataMethod import swagger
  from test.testdataMethod import sampleAPI

  idx = 0
  for frag in test_values :
    print(" - - - - - - - - - - - - - - ")
    soup = BeautifulSoup(frag)
#    if idx == 0 :
    if idx != -1 :
      processMethod(soup.body.contents[0], swagger, "OneOfTheTrelloEntities")
    idx = idx + 1

  print(">>  - - - - - - - - - - ?  - - - - - - - - - - -<<")
  print "JSON {}".format(json.dumps(swagger))
  print("<< - - - - - - - - - - - - - - - - - - - - - - ->>")

  TrelloAPI = json.loads(sampleAPI)
  TrelloAPI['paths'] = swagger['paths']

  # now write output to a file
  TrelloAPI_json = open("TrelloAPI_test.json", "w")
  TrelloAPI_json.write(json.dumps(TrelloAPI, indent=2, sort_keys=False))
  TrelloAPI_json.close()

if __name__ == "__main__": main()

