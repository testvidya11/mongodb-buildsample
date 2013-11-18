import pymongo

#make sure mongo service is running

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

#create database
db = client.test_database

#create table/collection
posts = db.posts

#create document/row
post = {"author": "Shippable", "text": "Demo"}

#inserting the row into table/database
post_id = posts.insert(post)

#retrieve the values from database
with client.start_request():
        cursor = posts.find()
        for result in cursor:
                print result

#deleting the data from table
        posts.remove()

#dropping the database
client.drop_database('test_database')

#end the connection
client.end_request()
