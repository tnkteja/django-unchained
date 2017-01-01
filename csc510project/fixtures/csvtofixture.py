#!/usr/bin/python

from csv import DictReader
from json import dump
from sys import argv

with open(argv[1],"r") as fr, open(argv[1].replace(".csv",".json"),'w') as fw:
		dump(list(DictReader(fr, delimiter=';')), fw)