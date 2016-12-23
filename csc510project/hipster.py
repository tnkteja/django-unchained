#!/usr/bin/python

todo = \
"""
Lot of things to do.
* Read models and create view sets
* setup the angularjs based frontend content
* somemeans to configure the data
"""
print todo

APP="csc510project"
lines=[
"#!/usr/bin/python",
""
]


for imports in [
				[
				],
				[
				 "from django.conf.urls import include, url",
				 "from django.contrib import admin",
				 "from rest_framework import routers"
				],
				[
				 "from "+APP+".views import *"
				]
			   ]:
	imports.sort()
	lines.extend(imports)
	lines.append('')

lines.append("rr=routers.DefaultRouter()")
models=["movie","critic","user"]
models.sort()
lines.extend([ "rr.register(r'%ss', %sViewSet)"%(model,model.capitalize()) for model in models])

lines.append(object)
with open("tmp.py","w") as f:
	print >> f, '\n'.join(lines)