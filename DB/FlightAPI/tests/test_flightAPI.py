import requests

class TestFlightAPI:
    def test_create(self):
        #Arrange
        data_in = {
            "plane":"137",
            "price":1000
        }
        data_expect = [{
            "plane":"137",
            "price":1000
        }]
        #Act
        response_post = requests.post("localhost:8080/flights",data=data_in)
        response_get = requests.get("localhost:8080/flights")
        #Assert
        assert data_expect==response_get.json()
