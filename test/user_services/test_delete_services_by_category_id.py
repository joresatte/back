from src.domain.setup import setupForGeneralServices
from src.domain.respuesta import response_service

def test_should_return_one_user_services_by_id():
    client= setupForGeneralServices()
   
    response = client.delete("/api/services/user_services/service_1/category_1")
    assert response.status == '200 OK'
    response= client.get("/api/services/user_services")
    assert response.json == response_service
    
