import pymongo

client = pymongo.MongoClient("mongodb+srv://shreyamihika1:12345@cluster0.a24ndub.mongodb.net/?retryWrites=true&w=majority")
db = client.virtusa

records=db.superwomen

d={"name":input("enter name"),"ph":int(input("enter phone number")),"mail":input("enter mailid")}
records.insert_one(d)
print("inserted successfully")
read=records.find()
for x in read:
    print(x)