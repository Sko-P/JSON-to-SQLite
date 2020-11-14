import sqlite3
import json
import re
import sys
class sqlj:
    def __init__(self, name, json, name_table):
        self.name_db = name
        self.json_file = json
        self.name_table = name_table

    def process(self):
        with open(self.json_file,'r',encoding="utf-8") as f:
            d = json.load(f)
        a = d[0].keys()
        a = str(a)
        
        a = a.partition("dict_keys([")[2].partition("])")[0]
        a = a.replace(" ","")
        a = a.replace("'","")
        a = a.split(',')
        
        types = []
        
        
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
                        indice = len(types) - 1
                        
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
        db1 = sqlite3.connect(self.name_db)
        cc = db1.cursor()

        creation_ins = "CREATE TABLE " + self.name_table + "("
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
        
        string_=""
        count = 0
        for j in a:
            print (j)
            string_ += ":"+j
            if(a.index(j) != (len(a) - 1)):
                string_ +=","
        print(string_)
        for i in d:

            cc.execute("INSERT INTO "+self.name_table+" VALUES ("+string_+")",i)
            db1.commit()
        
    def run_test(self):
        db1 = sqlite3.connect(self.name_db)
        cc = db1.cursor()
        cc.execute("SELECT * FROM "+self.name_table)
        print(cc.fetchall())

    def main(self):
        self.process()



if __name__ == "__main__":
    if (len(sys.argv) !=0):
        print(sys.argv[3])
        print(sys.argv[2])
        print(sys.argv[1])
        tablename = sys.argv[3]
        db_name = sys.argv[2]
        json_file_ = sys.argv[1]
        a = sqlj(db_name,json_file_,tablename)
        a.main()


