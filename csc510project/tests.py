from django.test import TestCase
from django.test.utils import setup_test_environment
setup_test_environment()
import unittest
from django.test import Client
# Create your tests here.


client = Client()

# Authentication
response = client.login(username="user",password="user")
#response = client.post('/api/authentication',{"username":"user","password":"user"})

print response