#!/usr/bin/env python
from bs4 import BeautifulSoup
from processMethod import processMethod
import urllib2
import json
import sys

#  Constants
TRELLO_JSON_FILE="TrelloAPI.json"

# Methods
def processTrelloEntity(soup, swagger, numEntity):
  entity = swagger['tags'][numEntity]['name']
  index = soup.html.body.find(class_='section', id=entity)
  for div in index.find_all("div", recursive=False) :
    print "Entity {}  --  {}".format(entity, div['id'])
    processMethod(div, swagger, entity)
    
  return
  
def processTrelloAPIIndex(soup, swagger):
  
  for link in soup.find_all(class_='toctree-l1') :
    swagger['tags'].append(
    {
        "name": link.a.string
      , "description": "{}/{}".format(swagger['info']['api_documentation'], link.a['href'])
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
      "description": "This document describes the REST API of Trello as published by Trello.com. <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>",
      "termsOfService": "https://trello.com/legal",
      "api_documentation": "https://trello.com/docs/api",
      "contact": {
        "name": "Trello",
        "url": "https://trello.com/home"
      },
      "license": {
        "name": "Trello : Terms of Service",
        "url": "https://trello.com/legal"
      }
    },
    "host": "api.trello.com",
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
    "paths": {
    },
    "basePath": "/1",
    "schemes": [
      "http"
    ],
    
  }
  
  soup = BeautifulSoup(urllib2.urlopen(swagger['info']['api_documentation']).read())
  processTrelloAPIIndex(soup, swagger)
  processTrelloToC(swagger)
  
  print(">> - - - - - - - - - - ! - - - - - - - - - - -<<")
  print "JSON {} written to {}".format(json.dumps(swagger['info']['title']), TRELLO_JSON_FILE)
  print("<< - - - - - - - - - - - - - - - - - - - - - ->>")

  # now write output to a file
  TrelloAPI_json = open(TRELLO_JSON_FILE, "w")
  # magic happens here to make it pretty-printed
  TrelloAPI_json.write(json.dumps(swagger, indent=2, sort_keys=False))
  TrelloAPI_json.close()
  
if __name__ == "__main__": main()

