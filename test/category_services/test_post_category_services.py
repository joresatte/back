from src.domain.setup import setupForPostedCategoryServices
from src.domain.respuesta import data_service, response_get_service

def test_return_category_services_posted():
    client= setupForPostedCategoryServices()
    data= data_service
    response= client.post('/api/services/by-category', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/by-category')
    assert response.json== response_get_service