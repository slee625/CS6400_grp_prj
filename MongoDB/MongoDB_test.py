import pymongo
import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CS6400_grp_prj"]
mycol = mydb["movies_metadata"]


import pymongo
x  = np.arange(100,40000,100)
y =  []
for i in range(100,40000,100):
  st = time.time()
  myresult = mycol.find().limit(i)
  print(len([x for x in myresult]))
  et = time.time()
  query_time = et - st
  y.append(query_time)

plt.figure()
plt.plot(x, y)
plt.legend(['Select N rows query'],loc='best',fontsize ='small')
plt.title('MongoDB SELECT N rows query time')
plt.xlabel('Number of rows')
plt.ylabel('query execution time')
plt.savefig('MongoDB_test_graph1')


