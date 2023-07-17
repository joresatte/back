from src.domain.utils import Utils

class Categories:
    def __init__(self, cat_id, text, text_pictures):
        self.cat_id = cat_id
        self.text = text
        self.text_pictures = text_pictures

    def to_dict(self):
        return {
            "cat_id": self.cat_id,
            "text": self.text,
            "text_pictures": self.text_pictures,
        }

class CategoriesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn= Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.TableTocreate(self, tableName= "categories", tables_variables= ['cat_id ', 'text', 'text_pictures'])
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from categories"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [Categories(**item) for item in data]
        return users

    def get_by_id(self, cat_id):
        sql = """SELECT * FROM users WHERE cat_id=: cat_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"cat_id": cat_id})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = Categories(**data)

        return user

    def save(self, category):
        sql = """insert into categories (cat_id, text,text_pictures) values (
            :cat_id, :text, :text_pictures
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {"cat_id": category.cat_id, "text": category.text, "text_pictures": category.text_pictures}
        )
        conn.commit()
