from src.domain.setup import setupForGeneralServices
from src.domain.respuesta import data_service, response_get_service

def test_should_return_one_user_services_by_id():
    client= setupForGeneralServices()
   
    response = client.get("/api/services/user_services/service_1")
    assert response.json == response_get_service

def test_should_return_one_user_services_by_id_cat_id_text():
    client= setupForGeneralServices()
   
    response = client.get("/api/services/user_services/service_1/category_1/Mudanzas")
    assert response.json == data_service
    
