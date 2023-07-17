from cgitb import text
from pyparsing import Regex
from flask import Flask, request
from flask_cors import CORS

from src.domain.category_services import  Category_services
from src.domain.users_services import  Services
from src.domain.regists import  Regists
from src.lib.utils import object_to_json
import re
import json

re_email= "[a-zA-Z0-9!#$%&'*_+-]([\.]?[a-zA-Z0-9!#$%&'*_+-])+@[a-zA-Z0-9]([^@&%$\/()=?¿!.,:;]|\d)+[a-zA-Z0-9][\.][a-zA-Z]{2,4}([\.][a-zA-Z]{2})?"

def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world(): 
        return "...magic!"

    @app.route("/api/object_services", methods=["GET"])
    def get_object_services():
        obj_service= repositories["object_services"].get_all_object_services()
        return obj_service

    @app.route("/api/categories", methods=["GET"])
    def get_all_categories():
        all_categories = repositories["categories"].get_all()
        return object_to_json(all_categories)

    @app.route("/api/services/user_services", methods=["GET"])
    def get_all_users_services():
        all_services = repositories["services"].get_all_services()
        return object_to_json(all_services)

    @app.route("/api/services/user_services/<id>", methods=["GET"])
    def get_user_services_by_id(id):
        service_by_id = repositories["services"].get_user_services_by_id(id)
        return object_to_json(service_by_id)

    @app.route("/api/services/user_services/<category_id>", methods=["GET"])
    def get_user_services_by_cat_id(cat_id):
        print('............', cat_id)
        service_by_cat_id = repositories["services"].get_user_services_by_cat_id(cat_id)
        return object_to_json(service_by_cat_id)
    
    @app.route("/api/services/user_services/<id>/<cat_id>/<text>", methods=["GET"])
    def get_services(id, cat_id, text):
        user_services = repositories["services"].get_service(id, cat_id, text)
        return object_to_json(user_services)
    
    @app.route("/api/services/user_services", methods=["POST"])
    def post_user_services():
        data= request.json
        user_services = Services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
        )
        if data['id'] or data["email"]!= '' or re.match(re_email, data["email"]):
           repositories["services"].save(user_services)
           return '', 200
        else:
            return '', 403

    @app.route("/api/services/by-category", methods=["GET"])
    def get_all_services_by_category():
        all_categories = repositories["categories_services"].get_all_services_by_category()
        return object_to_json(all_categories)

    @app.route("/api/services/by-category/<category_id>", methods=["GET"])
    def get_all_services_by_category_id(category_id):
        all_categories = repositories["categories_services"].get_category_services_by_cat_id(category_id)
        return object_to_json(all_categories)

    @app.route("/api/services/by-category", methods=["POST"])
    def post_category_services():
        data= request.json
        services_by_category = Category_services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
        )
        if data["email"]!= '' or re.match(re_email, data["email"]):
           repositories["categories_services"].save(services_by_category)
           return '', 200
        else:
            return '', 500

    @app.route("/api/regists", methods=["POST"])
    def post_regists():
        data= request.json
        print("-------------", data)
        user= Regists(
            id= data['id'],
            email= data['email'],
            password= data['password']
            )
        print("-----------", user)
        if (data['id'])!= '':
            if(data['email'])!= '' :
                if (data['password'])!= '':
                    if re.match(re_email, data['email']):
                       repositories["regists"].save(user)
                       return '', 200
        else:
            return 'invalid regist', 500

    @app.route("/api/regists", methods=["GET"])
    def get_all_regists():
        all_regists = repositories["regists"].get_all_regists()
        return object_to_json(all_regists)

    @app.route("/api/regists/<id>", methods=["GET"])
    def get_regist_by_id(id):
        regist = repositories["regists"].get_regist_by_id(id)
        print('-----el registro:', regist)
        return regist.to_dict()

    @app.route("/api/login/Authenticated", methods=["POST"])
    def get_login():
        data= request.json
        user= repositories["regists"].get_by_email_and_password(data['email'], data ['password'])
        if user is None or (data['password']) != user.password or (data['email']) != user.email:
            return 'invalid log In', 401
        else:
            return object_to_json(user)

    @app.route("/api/services/by-category/<id>/<cat_id>", methods=["DELETE"])
    def delete_category_service(id, cat_id):
        user = repositories["categories_services"].delete_category_services(id, cat_id)
        return "", 200

    @app.route("/api/services/user_services/<id>/<cat_id>", methods=["DELETE"])
    def delete_service(id, cat_id):
        service = repositories["services"].delete_services(id, cat_id)
        return "", 200
 
    @app.route("/api/services/by-category/<id>/<cat_id>/<text>", methods=["PUT"])
    def modify_category_service(id, cat_id, text):
        data = request.json
        if id!=data["id"] or cat_id!= data["cat_id"] or text!= data["text"]:
            return '', 403
        else:
            category_services = Category_services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
            )
            repositories["categories_services"].update_category_service(id , cat_id , text, category_services)
            return '', 200

    @app.route("/api/services/user_services/<id>/<cat_id>/<text>", methods=["PUT"])
    def modify_user_services(id, cat_id, text):
        data = request.json
        print('---------data_request', data)
        if id!=data["id"] or cat_id!= data["cat_id"] or text!= data["text"]:
            return '', 403
        else:
            user_services = Services(
            id= data["id"],
            cat_id= data["cat_id"],
            user_name= data["user_name"],
            text= data["text"],
            intro= data["intro"],
            price= data["price"],
            text_pictures= data["text_pictures"],
            textarea= data['textarea'],
            phone= data["phone"],
            email= data["email"],
            city= data["city"],
            )
            repositories["services"].update_service(id , cat_id , text, user_services)
            print('-----------user_services')
            return '', 200

    return app
