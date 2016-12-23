# #!/usr/bin/python
# from random import sample, random, randint
# from string import ascii_lowercase

# from django.test import Client, TestCase
# # Create your tests here.

# rstring=lambda :  ''.join(sample(ascii_lowercase, randint(1,25)))  

# class Account(TestCase):

# 	@classmethod
# 	def setUpClass(cls):
# 		cls.client=Client()

# 	def setUp(self):
# 		self.c = self.__class__.client

# 	def test_0_authentication_get(self):
# 		r = self.c.post('/api/authentication',{"j_username":"ntadiko","j_password":"passwordntadiko"})
# 		print r.status_code
# 		print r.content

# 	def test_1_account_get(self):
# 		r=self.c.get("/api/account")
# 		print r.status_code
# 		print r.json()

# 	def test_2_account_post(self):
# 	    r=self.c.post("/api/account",{"first_name": rstring(), "last_name": rstring(), "email": "ntadiko@ncsu.edu"})
# 	    print r.status_code
# 	    print r

# 	def test_3_account_change_password_post(self):
# 	    r=self.c.post("/api/account/change_password","ntadiko")
# 	    print r.status_code
# 	    print r.json()		

# 	def tearDown(self):
# 		pass

# 	@classmethod
# 	def tearDownClass(cls):
# 		pass