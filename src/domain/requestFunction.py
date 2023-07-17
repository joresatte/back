from src.domain.utils import Utils

class Resquest:
    def __init__(self, id, name, subject, comments):
        self.id= id
        self.name= name
        self.subject= subject
        self.comments= comments
        
    def to_dict(self):
        return {
            'received successfully'
        }
    
class RequestRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.createTable(self, tables_variables= ['id', 'name', 'subject', 'comments'], tableName= "requestables")
        conn= self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def save(self, request):
        sql = """insert or replace into requestables (id, name, subject, comments) values (
            :id, :name, :subject, :comments
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": request.id, "email": request.email, "password": request.password, "password": request.password}
        )
        conn.commit()
