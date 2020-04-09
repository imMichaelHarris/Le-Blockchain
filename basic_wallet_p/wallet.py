import requests
import sys
import json

print("Blockchain wallet")
name = input("Enter your name: ")
r = requests.post("http://localhost:5000/last_block")

print(f"Welcome {name}! Checking your balance now...")
