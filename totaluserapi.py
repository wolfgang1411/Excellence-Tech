import requests
import json

def totalUsers(totalPages):
    print("func start")
    accumulator = 0
    for num in range(1 , totalPages +1):
        print(f'checking page no : {num}')
        users = requests.get(f'https://reqres.in/api/users?page={num}').json()
        accumulator += len(users.get("data"))

    print(f'total no of users are : {accumulator}')

totalPages = int(input("enter total no of pages : "))
totalUsers(totalPages)