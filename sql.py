import sqlite3
import json
import re
 

#for i,j in zip(range(0,5),range(0,6)):
name_table = "rang"
a = "27/01/2004"
'''
if(a.isalpha()):
    print("its' text")
else:
    print("try02")
    if(a.contains("/") or a.contains(":")):
        print("its' a date")
'''
with open('dict.json','r',encoding="utf-8") as f:
    d = json.load(f)
    a = d[0].keys()
    a = str(a)
    #print(a)
    a = a.partition("dict_keys([")[2].partition("])")[0]
    a = a.replace(" ","")
    a = a.replace("'","")
    a = a.split(',')
    #print(a)
    #print(type(a[0]))
    types = []
    
    #print(len(d))
    for j in a:
        print(d[0][j])
        try:
            if(d[0][j].isalpha()):
                types.append("text")
                print("its' text")
            else:
                if((":" in d[0][j]) or ("-" in d[0][j])):
                    types.append("text")
                    print("its' a date")
                else:
                    print("its' a text i")
                    types.append("text")

        except AttributeError :
            if(isinstance(d[0][j], float)):
                    types.append("real")
                    print("its' a real")
            else:
                types.append("integer")
                print("its' a integer")
    print(types)
dict_ = {}

for i,j in zip(types,a):
    dict_[j] = i

print(dict_)


db1 = sqlite3.connect(':memory:')

cc = db1.cursor()

creation_ins = "CREATE TABLE " + name_table + "("
count = 0
for i,j in zip(types,a):
    creation_ins += j + " "+ i
    if(count != len(types) - 1):
        creation_ins += ","
        count += 1
creation_ins +=")"

print(creation_ins)


cc.execute(creation_ins)
db1.commit()
#db1.close()
string_=""
for j in a:
    string_ += ":"+j
    if(a.index(j) != (len(a) - 1)):
        string_ +=","
for i in d:
    
    '''   
        string_ += str(i[j])
        if(a.index(j) != (len(a) - 1)):
            string_ +=","
    print(string_)
    '''
    cc.execute("INSERT INTO "+name_table+" VALUES ("+string_+")",i)
    db1.commit()
cc.execute("SELECT * FROM "+name_table)
print(cc.fetchall())
db1.close()

'''

cc.execute("""CREATE TABLE medecine (
    name text,
    shelf text,
    price real

    )""")

db1.commit()
'''
    
'''
    if(isinstance(j,str)):
                print("it's an str")
            else:
                if(isinstance(j,int)):
                    print("it's an str")
            '''
'''
db_ = sqlite3.connect('medecine.db') #:memory: to run db from RAM

cc = db_.cursor()
'''
'''
cc.execute("""CREATE TABLE medecine (
    name text,
    shelf text,
    price real

    )""")
'''
'''
#cc.execute("ALTER TABLE medecine ADD time_add text")
db_.commit()
cc.execute("INSERT INTO medecine VALUES ('VITAMINE D','A02',500,datetime('now'))")
db_.commit()
cc.execute("SELECT * FROM medecine")
print(cc.fetchall())
'''
#print(cc.fetch()) #fetchmany/fetchall | These instructions are related to cc.execute 
#name = "Vitamine C"
#cc.execute("INSERT INTO medecine VALUES ('Vitamine C', 'A02', 120)")
'''
dict_ = {
"name" : "Zinc",
"shelf" : "B01",
"price" : 600 
}

a = dict_.keys()
print(a)
#Verify the type
'''

#cc.execute("INSERT INTO medecine VALUES (:name,:shelf,:price)",dict_)
#cc.execute("DELETE FROM medecine")
#cc.execute("INSERT INTO medecine VALUES (?,'A01',120)",(name,))
#db_.commit()
#cc.execute ("SELECT * FROM medecine")
#db_.commit()
#cc.execute("DELETE FROM medecine WHERE name=?",(name,))
#print(cc.fetchall())
#db_.close()