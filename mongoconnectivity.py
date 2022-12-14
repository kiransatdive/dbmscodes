
Q.13 Answer :---
//Save python code by “.py” 
// open in terminal & perform : python .\ connection.py 
// Connection  code :-
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
mydb=client["Satya"]
mycol=mydb["Students"]
data={'name':'Mobin','age':20}
mycol.insert_one(data)

data={'name':'Ram','age':40}
mycol.insert_one(data)

data={'name':'Lakhan','age':50}
mycol.insert_one(data)

data={'name':'Sumit','age':20}
mycol.insert_one(data)

data={'name':'Jeevan','age':21}
mycol.insert_one(data)

data={'name':'Samarth','age':23}
mycol.insert_one(data)

for data in mycol.find({}):
    print(data)
    print()


print("find Specific field ,using specific key and value:")
for data in mycol.find({'age':20}):
   print(data)
   print()


#Update /Edit Specific field ,using specific key ,method and values and update_one()

mycol.update_one(
     {'name':'Samarth'},
     {
         "$set":{
             'age':21
       }
     }
)

print("Updated the record ")
print()


#Delete / remove Specific field ,using specific key ,method and values and update_one()
mycol.delete_one({'name':'Jeevan'})
print("Deleted the record :Jeevan")
print()
