# @author: Jores Atte Mottoh
# @date: 14/07/2023
# @description: clase that contains useful methods 
# @project: Duty-place
# @modified by: 
# @modified date:
import sqlite3

class Utils:

    def create_conn(self):
        conn = sqlite3.connect(self)
        conn.row_factory = sqlite3.Row
        return conn
    
    # def getParameters(self, parameters, tableName):
    #     if parameters!= '' and tableName!= '':
    #         return parameters
	
    def createTable(self, tables_variables, tableName):
        requiredCeateString= 'create table if not exists'
        query= " "
        Query= ''
        if len(tables_variables)>0:
            for i in tables_variables:
                if i== 'id':
                    query+= requiredCeateString +' '
                    query+= tableName
                    query+='('
                    query+= i + ' ' + 'varchar primary key, '
                if i!= 'id':
                    query+= i + ' ' + 'varchar, '
        Query= query[:-2]+ ')'
        print('the query is:', Query)
        return Query
    
    def TableTocreate(self, tableName, tables_variables):
        requiredCeateString= 'create table if not exists'
        query= " "
        Query= ''
        if len(tables_variables)>0:
            for i in tables_variables:
                if 'id' in i and i!='id':
                    query+= requiredCeateString +' '
                    query+= tableName
                    query+='('
                    query+= i + ' ' + 'varchar primary key, '
                if 'id' not in i:
                    query+= i + ' ' + 'varchar, '
        Query= query[:-2]+ ')'
        print('the query is:', Query)
        return Query
