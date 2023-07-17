from src.domain.setup import setupForUpDatedRequest
from src.domain.respuesta import updater, updated, another_updater, another_one_updater

def test_return_valid_update_request():
    client= setupForUpDatedRequest()
    data= updater
    response= client.put('/api/services/user_services/service_1/category_1/Mudanzas', json= data)
    assert response.status== '200 OK' 
    response= client.get('/api/services/user_services/service_1')
    assert response.json== updated

def test_return_invalid_update_request():
    client= setupForUpDatedRequest()
    data= another_updater
    response= client.put('/api/services/user_services/service_1/category_1/Mudanzas', json= data)
    assert response.status_code== 403

def test_return_invalid_update_request():
    client= setupForUpDatedRequest()
    data= another_one_updater
    response= client.put('/api/services/user_services/service_1/category_1/Mudanzas', json= data)
    assert response.status_code== 403
    
    