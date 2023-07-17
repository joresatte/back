from src.domain.setup import setupForAuthentication
from src.domain.respuesta import another_one_login_request, login_request, login_response, another_login_request

def test_should_validate_user():
    client= setupForAuthentication()
    Body= login_request
    response = client.post("/api/login/Authenticated", json= Body)
    assert response.status_code == 200
    assert response.json== login_response

def test_should_invalidate_user():
    client= setupForAuthentication()
    Body= another_login_request
    response = client.post("/api/login/Authenticated", json= Body)
    assert response.status_code == 401

def test_should_invalidate_user():
    client= setupForAuthentication()
    Body= another_one_login_request
    response = client.post("/api/login/Authenticated", json= Body)
    assert response.status_code == 401

