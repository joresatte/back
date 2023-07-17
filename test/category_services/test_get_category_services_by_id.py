from src.domain.setup import setupForGeneralCategoryServices
from src.domain.respuesta import response_get_service

def test_should_return_services_list_by_category_id():
    client= setupForGeneralCategoryServices()
    
    response = client.get("/api/services/by-category/category_1")
    assert response.json == response_get_service
