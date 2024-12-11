from utils.env import BASE_URL
import requests




async def CreateUser(user_data):
    url = f'{BASE_URL}/users/'
    
    response = requests.post(url, json=user_data)

    if response.status_code in (200, 201):  
        print("Ma'lumot muvaffaqiyatli:", response.json())
    else:
        print("Xato:", response.status_code, response.text)
    return response.json()
    
            
            
def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return False

    