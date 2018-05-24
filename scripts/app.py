from flask import Flask,request,Response
import json
from utils import *
app = Flask(__name__)
@app.route('/loginUser', methods=['POST'])
def loginUser():
    user =  request.form['username']
    password = request.form['password']
    query = 'SELECT * FROM users'
    users = connect(query,True)
    valid_user = checkUsers(users, user, password)
    if(valid_user == True):
        response = Response(json.dumps('{"status" : "success","code":"1","message":"User authentication successful"}'))
        response.headers['Content-type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
    else:        
        response = Response(json.dumps('{"status" : "failure","code":"2","message":"User authenctication not successful"}'))
        response.headers['Content-type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/submitArticle', methods=['POST'])
def submitArticle():
    writer_name = request.form['writerName']
    article_title = request.form['articleTitle']
    article = request.form['article']
    query = "insert into articles (writer_name, article_title, article) values('"+ writer_name +"','"+ article_title +"','"+ article +"') returning id"
    print(query)
    save_article = connect(query)
    response = Response(json.dumps('{"status" : "success"}'))
    response.headers['Content-type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
if __name__ == "__main__":
	app.run(ssl_context='adhoc',debug=True)
