'''
Created on 18.12.2015

@author: rleber
'''
from pymysql.cursors import Cursor

class Database():

    def __init__(self,db, csv_data):
        print('initdb')
        self.db = db
        self.cursor = db.cursor()
        self.csv_data = csv_data
        self.tableName = ""
        
    def createTable(self, tableKey, attNameKey, attTypeKey, dataKey, databasename):
        attNameList= []
        attTypeList= []
        dataList= []
        attributes = ""
        attributeNames = ""
        data= ""
        colTmp= ""
        
        for row in self.csv_data:
            
            #Parsing for the table name
            if row[0] == tableKey:
                self.tableName = row[1]
                #print(tableKey)
                
            #Parsing for the attribute names
            if row[0] == attNameKey:
                for col in row:
                    if col != attNameKey: 
                        attNameList.append(col)
                        
            #Parsing for the attribute types
            if row[0] == attTypeKey:
                for col in row:
                    if col != attTypeKey:
                        attTypeList.append(col.replace("num", "numeric").replace("[","(").replace("]",")")+ ",")
                    
            #Parsing for data
            if row[0] == dataKey:
                for col in row:
                    if col != dataKey:
                        colTmp = col.replace("'","")
                        data =data + "'" + colTmp.replace("\"", "").replace("  ", "").replace("' ", "'") + "'" + ", "
                data = data[:-2]
                dataList.append(data)
                print(data)
                data = ""                   
        
        #Merging attribute names and types to one string and creating a string with all attribute names
        for string in range(len(attNameList)):
            attNameTmp=attNameList.pop(0)
            attributeNames=attributeNames+attNameTmp+','
            attributes = attributes+attNameTmp
            attributes = attributes+attTypeList.pop(0)
        attributeNames=attributeNames[:-1]
        attributes=attributes[:-1]
        
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS " +databasename)            
            self.cursor.execute("USE " +databasename)
            self.cursor.execute("DROP TABLE IF EXISTS "+self.tableName)      
            self.cursor.execute("CREATE TABLE "+self.tableName+"("+attributes+")")
        except Cursor.Error as err:
            print(err)
        
        for content in dataList:
            try:    
                self.cursor.execute("INSERT INTO "+self.tableName+"("+attributeNames+") VALUES("+content+")")
            except Cursor.Error as err:
                print(err)
        dataList = []
        self.db.commit()
        
        
        
        