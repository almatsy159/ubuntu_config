import os
from flask import Flask,jsonify,request,render_template
import config
import json
import sqlite3 as sql
import sys


args = sys.argv
nb_args = len(args)
# allow to launch with arguments like config file ?


# connect to database (creates file if it doesn't exist)
conn = sql.connect("local.db")

# cursor allows executing SQL
cursor = conn.cursor()




class File():
    # import linuxfile !
    pass 

class Project():
    json_project = {}
    # kwargs => nosql ?
    def __init__(self,name:str,path="/",host="localhost",port=None,comment="", **kwargs):
        self.json_project["name"] = name
        self.json_project["path"] = path
        self.json_project["host"] = host
        self.json_project["comment"] = comment
        self.json_project["port"] = port
        
        for k,v in kwargs:
            self.json_project[k] = v


# # creation de type valable !
# def make_dir(name):
#     os.mkdir(name)
    
class Save():
    def __init__(self,name,date,path,support):
        self.name = name
        self.date = date
        self.path = path 
        self.support = support
    
    def next_save(self):
        pass
    # from last save date to now 
    
        
        

app = Flask(__name__)

try:
    with open("debug","r"):
        pass
    debug = True
except :
    debug = False
routes = config.routes
    

@app.route("/home")
def home():
    data = {
        "html":{
            "header":{"name":"header_data","routes":routes},
            "footer":"footer_data",
            "body":"body_data"},
        
        "source":"index",
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "args": request.args,
        "json": request.get_json(silent=True)}

    
    return render_template("index.html",data=data)


@app.route("/test")
def test():
    data = {
        "routes":f"{routes}",
        "source":"test",
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "args": request.args,
        "json": request.get_json(silent=True)}
    
    return render_template("test.html",data=data)

    
@app.route("/project", methods=["POST"])
def new_project():

    name = request.form.get("name")
    port = request.form.get("port")
    host = request.form.get("host")
    path = request.form.get("path")
    comment = request.form.get("comment")



    return f"Received: {name} at {host}:{port} {path}\n comment : {comment}"


# -------------------------
# GET with query parameters
# -------------------------
#  GET /search?name=John&age=30
#  curl -H "X-API-KEY: my-secret-key" \
# "http://localhost:5000/search?name=John&age=30"

@app.route("/search", methods=["GET"])
def search():

    name = request.args.get("name")
    age = request.args.get("age")

    return jsonify({
        "route": "search",
        "method": request.method,
        "params": {
            "name": name,
            "age": age
        }
    })
    
# -------------------------
# Path parameter
# -------------------------
# GET /user/42
# curl -H "X-API-KEY: my-secret-key" \
# http://localhost:5000/user/42

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):

    return jsonify({
        "route": "get_user",
        "user_id": user_id,
        "method": request.method
    })


@app.route("/send-http-request", methods=["POST"])
def send_request():

    host = request.form["host"]
    port = request.form["port"]
    method = request.form["method"]
    path = request.form["path"]

    header_name = request.form["header_name"]
    header_value = request.form["header_value"]
    body = request.form["body"]

    print(host, port, method, path)

    return "Request received"
    
    


@app.route("/project",methods=["POST"])
def new_with_route():
    return "new project with route here ! not implemented ! "

def new_without_route():
    return "new project without route here ! not implemented ! "



if __name__ == "__main__":
    # create table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,name TEXT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY,name TEXT,port INT DEFAULT NULL,path TEXT DEFAULT NULL,comment TEXT DEFAULT NULL)")
    
    # # date ,path , support_id
    # cursor.execute("CREATE TABLE IF NOT EXISTS saves (id INTEGER PRIMARY KEY,name TEXT,date DATETIME DEFAULT NOW())")
    
    #supports : description

    app.run(host=config.host,port=config.port,debug=debug)

