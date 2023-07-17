from src.domain.utils import Utils
class Regists:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
        }


class RegistsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.createTable(self, tables_variables= ['id', 'email', 'password'], tableName= "registros")
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_regist_by_id(self, id):
        sql = """SELECT * FROM registros WHERE id= :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Regists(
                id= data['id'],
                email= data['email'],
                password= data['password']
            )

        return user

    def get_by_email_and_password(self, email, password):
        sql = """SELECT * FROM registros WHERE email= :email AND password= :password"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"email": email, "password": password})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Regists(
                id= data['id'],
                email= data['email'],
                password= data['password']
            )

        return user

    def save(self, user):
        sql = """insert or replace into registros (id, email, password) values (
            :id, :email, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"id": user.id, "email": user.email, "password": user.password}
        )
        conn.commit()



