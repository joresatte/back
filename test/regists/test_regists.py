from src.domain.setup import setupForAuthentication
from src.domain.respuesta import regist_request, regist_response, another_regist_request

def test_should_return_status_code_200_for_regist_post():
    client= setupForAuthentication()
    Body= regist_request
    response = client.post("/api/regists", json= Body)
    assert response.status_code == 200
    response = client.get("/api/regists/service_1")
    assert response.json== regist_response

def test_should_return_access_not_allowed():
    client= setupForAuthentication()
    Body= another_regist_request
    response = client.post("/api/regists", json= Body)
    assert response.status_code == 500