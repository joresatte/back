from src.domain.setup import setupForGeneralCategoryServices
from src.domain.respuesta import response_service

def test_should_return_one_user_services_by_id():
    client= setupForGeneralCategoryServices()
   
    response = client.delete("/api/services/by-category/service_1/category_1")
    assert response.status == '200 OK'
    response= client.get("/api/services/by-category")
    assert response.json == response_service
    
