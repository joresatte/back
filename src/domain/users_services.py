from src.domain.utils import Utils
class Services:
    def __init__(self, id, cat_id, user_name, text, intro, price, text_pictures, textarea, email, phone, city):
        self.id= id
        self.cat_id= cat_id
        self.user_name= user_name
        self.text= text
        self.intro= intro
        self.price= price
        self.text_pictures= text_pictures
        self.textarea= textarea
        self.email= email
        self.phone= phone
        self.city= city

    def to_dict(self):
        return {
            "id": self.id,
            "cat_id": self.cat_id,
            "user_name": self.user_name,
            "text": self.text,
            "intro": self.intro,
            "price": self.price,
            "text_pictures": self.text_pictures,
            "textarea": self.textarea,
            "email": self.email,
            "phone": self.phone,
            "city": self.city,
        }

class ServicesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = Utils.create_conn(self.database_path)
        return conn

    def init_tables(self):
        sql = Utils.createTable(self, 
                tables_variables= ['id', 
                                   'cat_id', 
                                   'user_name', 
                                   'text', 
                                   'intro', 
                                   'price',
                                   'text_pictures',
                                   'textarea',
                                   'phone',
                                   'email',
                                   'city'], tableName= "services")
     
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_services(self):
        sql = """select * from services"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        services = []
        for item in data:
            users_services = Services(
                id= item["id"],
                cat_id= item["cat_id"],
                user_name= item["user_name"],
                text= item["text"],
                intro= item["intro"],
                price= item["price"],
                text_pictures= item["text_pictures"],
                textarea= item['textarea'],
                phone= item["phone"],
                email= item["email"],
                city= item["city"],
            )
            services.append(users_services)
        return services

    def get_user_services_by_id(self, id):
        sql = """SELECT * FROM services WHERE id= :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id":id})
        data = cursor.fetchall()
        services = []
        for item in data:
            if data is None:
                user_service = None
            else:
                user_service = Services(
                    id= item["id"],
                    cat_id= item["cat_id"],
                    user_name= item["user_name"],
                    text= item["text"],
                    intro= item["intro"],
                    price= item["price"],
                    text_pictures= item["text_pictures"],
                    textarea= item['textarea'],
                    phone= item["phone"],
                    email= item["email"],
                    city= item["city"],
                )
                services.append(user_service)
        return services

    def get_user_services_by_cat_id(self, cat_id):
        sql = """SELECT * FROM services WHERE cat_id= :cat_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"cat_id":cat_id})
        data = cursor.fetchall()
        services = []
        for item in data:
            user_service = Services(
                id= item["id"],
                cat_id= item["cat_id"],
                user_name= item["user_name"],
                text= item["text"],
                intro= item["intro"],
                price= item["price"],
                text_pictures= item["text_pictures"],
                textarea= item['textarea'],
                phone= item["phone"],
                email= item["email"],
                city= item["city"],
            )
            services.append(user_service)
        return services

    def delete_services(self, id, cat_id):
        sql = """ DELETE FROM services
                  WHERE id = :id and cat_id = :cat_id 
              """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id": id,
                  "cat_id": cat_id,
                  }
        )
        conn.commit()

    def update_service(self, id, cat_id, text, user_service):
        sql = """ UPDATE services
                    SET 
                    id= :id,
                    cat_id= :cat_id,
                    user_name= :user_name,
                    text= :text,
                    intro= :intro,
                    price= :price,
                    text_pictures= :text_pictures,
                    textarea= :textarea,
                    phone= :phone,
                    email= :email,
                    city= :city
                    WHERE id = :id and cat_id = :cat_id and text= :text """
        conn = self.create_conn()
        cursor = conn.cursor()
        params = user_service.to_dict()
        params["id"] = id
        params["cat_id"] = cat_id
        params["text"] = text
        cursor.execute(sql, params  )
        conn.commit()

    def get_service(self, id, cat_id, text):
        sql = """SELECT * FROM services 
                 WHERE id = :id and cat_id = :cat_id and text = :text
              """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, 
            {
                "id": id,
                "cat_id": cat_id,
                "text": text
            }
        )
        data = cursor.fetchone()
        if data is not None:
             user_service = Services(**data)
        else:
            user_service = None

        return user_service

    def save(self, user_service):
        sql = """INSERT INTO services (id, cat_id, user_name, text, intro, price, text_pictures, textarea, phone, email, city) values (
            :id, :cat_id, :user_name, :text, :intro, :price, :text_pictures, :textarea, :phone, :email, :city
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            user_service.to_dict(),
        )
        conn.commit()
