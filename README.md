# trello-swagger-generator
Reads Trello's crappy API documentation pages and generates a swagger file.


### to generate the swagger

     pip install beautifulsoup4
     ./generate_swagger_TrelloAPI.py

### to view the swagger file
#### run the simple Python http server

     dev/http_cors_server.py

Open your browser to [localhost:8000](http://localhost:8000)

![Imgur](http://i.imgur.com/cK1V7MU.png)


#### obtain and run the swagger.io viewer

    cd ~/projects
    wget -O swagger.zip https://github.com/swagger-api/swagger-ui/archive/master.zip
    unzip swagger.zip
    mv swagger-ui-master swagger-ui
    mv swagger.zip swagger-ui
    cd swagger-ui
    
edit `dist/index.html` line #32 replacing ...

    url = "http://petstore.swagger.io/v2/swagger.json";
 
 ... with ...
 
    url = "http://localhost:8000/TrelloAPI.json";
 
Open a second tab in your browser to the local file address file :

    file:///home/yourself/projects/swagger-ui/dist/index.html
 
 

![Imgur](http://i.imgur.com/CEvWdyn.png)








 
