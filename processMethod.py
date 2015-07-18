#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from processArguments import processArguments
import json
import sys
import re

#  Constants
REQUIRED_PERMISSIONS="Required permissions:"
NOTES = "Notes:"

debugPrint = False

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

def fixFieldName(theField) :  # get first full word and if _id is a suffix make it a prefix
  split_field = theField.split()

  field = split_field[0]
  if "_id" in field :
    field = field.replace('_id', '')
    field = 'id{}'.format(field.title())

  if len(split_field) > 1 and "id" in split_field[1] :
    field = 'id{}'.format(field.title())

  return field

def preparePath(path, basePath) :  # detect/prepare and flag the contained path parmeters

  namePath = path.replace('[', '{').replace(']', '}').strip()
  namePath = namePath.replace(basePath, '')
  fields = []
  for span in re.finditer('\[(.*?)\]', path):
    aField = path[span.start()+1:span.end()-1]
    nameField = fixFieldName(aField)
    namePath = namePath.replace(aField, nameField)
#    print '{} - ({} vs {})'.format(namePath, aField, nameField)
    fields.append({nameField : aField})

  return {"namePath" : namePath, "fields" : fields }



http2crud = {'get' : 'get', 'post' : 'add', 'put' : 'update', 'delete' : 'delete'}
def makeOperationId(method, defPath) :  # get first full word and if _id is a suffix make it a prefix
  bits = defPath["namePath"].split('/')
  parms = []
  nouns = []
  for bit in bits :
    if '{' in bit :
      parm = bit.strip().replace('{', '').replace('}', '')
      parms.append('{}{}'.format(parm[:1].title(), parm[1:]))
    else :
      noun = bit.strip()
      nouns.append('{}{}'.format(noun[:1].title(), noun[1:]))

    parmClause = 'By'.join(parms)
    if len(parmClause) > 0 :
      parmClause = 'By{}'.format(parmClause)
    operationId = '{}{}{}'.format(http2crud[method], ''.join(nouns), parmClause)

  if debugPrint : print 'Operation Id : {}\n\n'.format(operationId)
  return operationId


def processMethod(soup, swagger, entity):

  '''
  print "# {}".format(soup)
  sys.exit()
  '''
  defPath = preparePath(soup.h2.span.text, swagger["basePath"])
  namePath = defPath["namePath"]
  nameMethod = soup.h2.next_element.lower().strip()


  cursor = {'entity' : entity, 'path' : namePath, 'method' : nameMethod}

  if cursor['entity'] == "cardxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
    and cursor['method'] == "delete":
      debugPrint = True
  else:
      debugPrint = False


  print "Method : {}, Path : {}".format(nameMethod, namePath)
#  if debugPrint : print "Method : {}, Path : {}".format(nameMethod, namePath)

  if   namePath not in swagger['paths'] :
                                swagger['paths'][namePath] = {}
  if nameMethod not in swagger['paths'][namePath] :
                    swagger['paths'][namePath][nameMethod] = {"tags" : [entity]}


  swagger['paths'][namePath][nameMethod]['operationId'] = makeOperationId(nameMethod, defPath)
  swagger['paths'][namePath][nameMethod]['summary'] = '{}()'.format(swagger['paths'][namePath][nameMethod]['operationId'])

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
  processArguments(arguments, swagger, defPath["fields"], cursor)

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

