from third_party.requests import requests
from pprint import pprint

def add(a, b):
    res = requests.get(f"https://www.wolframalpha.com/n/v1/api/autocomplete/?i={a}+%2B+{b}")
    return res.json()["instantMath"]["exactResult"]
