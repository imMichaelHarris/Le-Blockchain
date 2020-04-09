import requests
import sys
import json

print("Blockchain wallet")
name = input("Enter your name: ")

print(f"Welcome {name}! Checking your balance now...")
r = requests.post(f"http://localhost:5000/me", json=name)
data = r.json()
print(data)
