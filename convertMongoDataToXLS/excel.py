import xlwt
import random
from pymongo import MongoClient
client = MongoClient()
db = client['test']
collection = db['user']
#for id in range(2,10):
#	name = random.choice(["email","email2","email3"])
#	age = random.choice([23,12,45,55])
#	sex = random.choice(['female','male'])
#	collection.insert({'name': name,'age': age, 'sex': sex})
book = xlwt.Workbook(encoding='utf-8',style_compression = 0)
table = book.add_sheet('data-1')
cdata = collection.find()
lenth = collection.count()
print lenth
#for data in collection.find():
#	print data
count = 0
for data in cdata:
	print type(data)
	print data.keys()
	name = ''
	age = ''
	sex = ''
	if data.has_key('name'):
		name = data['name']
	if data.has_key('age'):
		age = data['age']
	if data.has_key('sex'):
		sex = data['sex']
	table.write(count,0,name)
	table.write(count,1,age)
	table.write(count,2,sex)
	count += 1
#table.write(1,0,'test2')
book.save('book.xls')
