#!/usr/bin/env python
from bs4 import BeautifulSoup
from processMethod import processMethod
import urllib2
import json
import sys

#  Constants
TRELLO_JSON_FILE="TrelloAPI.json"
API_DOC = "https://trello.com/docs/api"

# Methods
def processTrelloEntity(soup, swagger, numEntity):
  entity = swagger['tags'][numEntity]['name']
  '''
#  print "Entity {} ".format(entity)
#  if "board" in entity :
  if "action" in entity :
#  if "label" in entity :
#  if "member" in entity :
    print "Doing {}".format(entity)
  else:
    return
  '''
  index = soup.html.body.find(class_='section', id=entity)
  for div in index.find_all("div", recursive=False) :
#    print "Entity {}  --  {}".format(entity, div['id'])
    processMethod(div, swagger, entity)

  return

def processTrelloAPIIndex(soup, swagger):

  for link in soup.find_all(class_='toctree-l1') :
    swagger['tags'].append(
    {
        "name": link.a.string
      , "description": "{}/{}".format(API_DOC, link.a['href'])
    })

  return

def processTrelloToC(swagger):

  idx = 0
  for tag in swagger['tags'] :
    if idx != 101 :
#      print "{}".format(tag['description'])
      processTrelloEntity(
          BeautifulSoup(urllib2.urlopen(tag['description']).read())
        , swagger
        , idx
      )
    idx = idx + 1

  return


#  -   -   -   -   -   -   -   -   -   -   -
#  Main routine (for testing)
def main():

  swagger = {
    "swagger": "2.0",
    "info": {
      "version": "1.0",
      "title": "Trello API",
      "description": "This document describes the REST API of Trello as "
         + "published by Trello.com."
         + "\n - <a href='https://trello.com/docs/index.html' target='_blank'>"
         + "Official Documentation</a>"
         + "\n - <a href='" + API_DOC + "' target='_blank'>"
         + "The HTML pages that were scraped in order to "
         + "generate this specification.</a>",
      "termsOfService": "https://trello.com/legal",
      "contact": {
        "name": "Trello",
        "url": "https://trello.com/home"
      },
      "license": {
        "name": "Trello : Terms of Service",
        "url": "https://trello.com/legal"
      }
    },
    "host": "trello.com",
    "tags": [
    ],
    "securityDefinitions": {
      "trello_auth": {
        "type": "oauth2",
        "authorizationUrl": "https:\/\/trello.com\/1\/appKey\/generate",
        "flow": "implicit",
        "scopes": {
          "write:boards": "modify any of the boards in your account",
          "read:boards": "read any of the boards in your account"
        }
      },
      "api_key": {
        "type": "apiKey",
        "name": "api_key",
        "in": "header"
      }
    },
    "definitions": {
    },
    "paths": {
    },
    "basePath": "/1",
    "schemes": [
      "https"
    ],

  }

  soup = BeautifulSoup(urllib2.urlopen(API_DOC).read())
  processTrelloAPIIndex(soup, swagger)
  processTrelloToC(swagger)

  print(">> - - - - - - - - - - ! - - - - - - - - - - -<<")
  print "JSON {} written to {}".format(json.dumps(swagger['info']['title']), TRELLO_JSON_FILE)
  print("<< - - - - - - - - - - - - - - - - - - - - - ->>")

  # now write output to a file
  TrelloAPI_json = open(TRELLO_JSON_FILE, "w")

  # magic happens here to make it pretty-printed
  prettySpec = json.dumps(swagger, indent=2, sort_keys=False)

  # replace all "false" with false and all "true" with true
  finalSpec = prettySpec.replace("\"false\"", "false").replace("\"true\"", "true")

  TrelloAPI_json.write(prettySpec)
  TrelloAPI_json.close()

if __name__ == "__main__": main()

      # "List":{
      #   "type":"object",
      #   "properties":{
      #     "name":{
      #       "type":"string"
      #     },
      #     "pos":{
      #       "type":"string",
      #       "default":"top"
      #     }
      #   },
      #   "xml":{
      #     "name":"Order"
      #   }
      # }
