import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Define the URL, JSON_STRING, and CONVERTED_DATA
URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
JSON_STRING = '[{"name": "Daniel", "occupation": "LG Fridge Salesman"}, ...]'  # Define your expected JSON as a string
CONVERTED_DATA = [...]  # Define your expected converted data

# Define the test function
def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    response_body = requester.get_response_body().strip()  # Remove extra whitespace
    assert response_body == JSON_STRING.strip()

def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    converted_data = requester.load_json()
    assert converted_data == CONVERTED_DATA

# Run the tests
if __name__ == "__main__":
    test_get_response()
    test_load_json()
