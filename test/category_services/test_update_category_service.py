from src.domain.setup import setupForUpdatedCategoryServices
from src.domain.respuesta import updater, updated

def test_return_category_services_edited():
    client= setupForUpdatedCategoryServices()
    data= updater
    response= client.put('/api/services/by-category/service_1/category_1/Mudanzas', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/by-category/category_1')
    assert response.json== updated