import json
import requests

SERVER_URL = "https://protected-everglades-36173.herokuapp.com"
ADD_URL = "%s/add" % SERVER_URL
DATA_URL = "%s/datadump" % SERVER_URL

def test_post():
    json = {"id": "test_python_id", "data": "test_data"}
    r = requests.post(ADD_URL, json)
    r.raise_for_status()

def get_data():
    r = requests.get(DATA_URL)
    r.raise_for_status()
    data = json.loads(r.text)

    for result in data:
        print result["id"]
        print result["data"]

def main():
    test_post()
    get_data()

if __name__ == "__main__":
    main()
