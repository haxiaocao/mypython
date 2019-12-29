from pymongo import MongoClient

# reference:https://api.mongodb.com/python/current/examples/authentication.html#scram-sha-1-rfc-5802
uri = "mongodb://guokaitest:testgk123@localhost:10123/?authSource=testDB&authMechanism=SCRAM-SHA-1"
client = MongoClient(uri)

# client = MongoClient('127.0.0.1:10123',
#                      username='guokaitest',
#                      password='testgk123',
#                      authSource='testDB',
#                      authMechanism='SCRAM-SHA-1')

# Note: db name is case sensitive.
db = client.testDB
employee = {"id": "105",
            "name": "Peter",
            "profession": "Software Engineer",
            }
emps = db.employees
emps.insert_one(employee)
print(emps.find_one())

with client:
    print(db.collection_names())

with client:
    ems=db.employees
    ems_find=ems.find()
    #print(list(ems_find))
    #print("........")
    #print(ems_find.next())
    #print(ems_find.next())
    print(type(ems_find))
    print(ems_find.count())

    for em in ems_find:
        print(em)

exp_cardsdb=db.employees.find({'name':'Peter'})
with client:
    ems=db.employees
    ems_find=ems.find({},{'_id':1,'profession':1})
    for em in ems_find:
        print(em)


