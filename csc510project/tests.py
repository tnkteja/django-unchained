# from django.test import TestCase
# from django.test.utils import setup_test_environment
# setup_test_environment()
# import unittest
from json import loads
from random import sample, random, randint
from string import ascii_lowercase

from django.test import Client, TestCase
# Create your tests here.

c = Client()

# # Authentication
# r = c.post('/api/authentication',{"j_username":"user3","j_password":"ntadiko1"})
# print r.status_code
# print r.content
# print '-'*32
# r=c.get("/api/account")
# print r.status_code
# print r.content
# print '-'*32
# rstring=lambda :  ''.join(sample(ascii_lowercase, randint(1,25)))
# r=c.post("/api/account",{"first_name": rstring(), "last_name": rstring(), "email": "ntadiko@ncsu.edu"})
# print r.status_code
# print '-'*32
# r=c.post("/api/account/change_password",{"new_password":"ntadiko1"})
# print r.status_code

# print '-'*32
# r=c.post("/api/register",{"username":rstring(),"email": "ntadiko@ncsu.edu","password":"ntadiko"})
# print r.status_code
# print r.content

print '-'*32
r=c.get("/api/movies/public/")
print r.status_code
print r.content