def test_login(client):
    response = client.post(
        "/auth/login", json={"email": "adele.gaudry@gmail.com", "password": "ramen"}
    )
    assert response.status_code == 200
