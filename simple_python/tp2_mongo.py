import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["empresa"]
mycol = mydb["productos"]

mycol.insert_one({'codigo': 9876, 'nombre':'CARAMELOS MASTICABLES', 'precio':1000.00})

for producto in mycol.find():
  print(producto['nombre'])