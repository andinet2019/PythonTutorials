import flask
from flask import request,jsonify
import sqlite3
app = flask.Flask(__name__)
app.config["DEBUG"] = True
def dict_factory(cursor,row):
    d={}
    for idx, col in enumerate(cursor.description):
        d[col[0]]=row[idx]
    return d
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

def api_all():
    conn=sqlite3.connect('books.db')
    conn.row_factory=dict_factory()
    cur=conn.cursor()
    all_books=cur.execute("SELECT *FROM books;").fetchall()
    return jsonify(all_books)
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
@app.route('/api/v1/resources/books',methods=['GET'])
def api_filter():
    query_parrameters=request.args
    id=query_parrameters.get('id')
    published=query_parrameters.get('published')
    author=query_parrameters.get('author')
    query="SELECT * FROM books WHERE"
    to_filter=[]
    
app.run()