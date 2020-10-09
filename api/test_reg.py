import requests
url = "http://127.0.0.1:8000/authentication/signup/"

data = {
        "first_name": "reques_T444o",
        "middle_name": "",
        "last_name": "Galilei",
        "email": "andt@gmail.com",
        "password": "pbkdf2_sha256$216000$yM15ip6Aeinn$CjNR9cwab",
        "updated_at": "2020-10-03T15:16:04.587154Z",
        "created_at": "2020-10-03T15:16:04.587154Z",
        "role": 0,
        "is_active": True,
        "is_staff": True
    }


responce = requests.post(url=url, json=data)
print(responce)