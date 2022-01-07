from flask import Flask, render_template, request, Response, redirect, url_for
from elasticsearch import Elasticsearch
import pandas as pd
import sqlite3

app = Flask(__name__)

es = Elasticsearch()
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
  book_user_likes = request.form.get("book_user_likes")
  if book_user_likes is not None:
    resp = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": book_user_likes,
                "fields": ["Title"]}})
  book_id = resp['hits']['hits'][0]['_source']['Id']
  cos_sim = pd.read_csv("cos_sim.csv", skiprows = int(book_id) + 1, nrows=1, header=None)
  cos_sim_list = list(cos_sim.iloc[0, 1:])
  similar_books = list(enumerate(cos_sim_list)) 
  sorted_similar_books = sorted(similar_books,key=lambda x:x[1],reverse=True)[0:]
  book_1 = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": sorted_similar_books[2][0]-1,
                "fields": ["Id"]}})
  book_2 = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": sorted_similar_books[6][0]-1,
                "fields": ["Id"]}})
  book_3 = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": sorted_similar_books[3][0]-1,
                "fields": ["Id"]}})
  book_4 = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": sorted_similar_books[4][0]-1,
                "fields": ["Id"]}})
  book_5 = es.search(index="books", doc_type="_doc", query =  {"multi_match": {
                "query": sorted_similar_books[5][0]-1,
                "fields": ["Id"]}})
  book_1 = book_1['hits']['hits'][0]['_source']['Title']
  book_2 = book_2['hits']['hits'][0]['_source']['Title']
  book_3 = book_3['hits']['hits'][0]['_source']['Title']
  book_4 = book_4['hits']['hits'][0]['_source']['Title']
  book_5 = book_5['hits']['hits'][0]['_source']['Title']

  conn = sqlite3.connect('books.db')
  cur = conn.cursor()
  cur.execute("SELECT `Url of image` FROM titles WHERE Title= (?) ", ((book_1,)))
  image_1 = cur.fetchall()
  cur.execute("SELECT `Url of image` FROM titles WHERE Title= (?) ", ((book_2,)))
  image_2 = cur.fetchall()
  cur.execute("SELECT `Url of image` FROM titles WHERE Title= (?) ", ((book_3,)))
  image_3 = cur.fetchall()
  cur.execute("SELECT `Url of image` FROM titles WHERE Title= (?) ", ((book_4,)))
  image_4 = cur.fetchall()
  cur.execute("SELECT `Url of image` FROM titles WHERE Title= (?) ", ((book_5,)))
  image_5 = cur.fetchall()


  return render_template('result.html', book_1 = book_1, book_2 = book_2, book_3 = book_3, book_4 = book_4, book_5 = book_5, image_1=image_1[0][0], image_2=image_2[0][0], image_3=image_3[0][0], image_4=image_4[0][0], image_5=image_5[0][0])

if __name__ == '__main__':
   app.run(debug=True)