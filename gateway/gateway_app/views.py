# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views import generic
import json
import time
import pymysql as mysql

# Create your views here.
conn = mysql.connect(user='root', password='ustcpof', database='gateway')
conn.autocommit(True)
cursor = conn.cursor()
tmp_time=0
idcount = 0

def rate(request):
	return render(request, 'demo.html')

def data(request):
	global tmp_time


	if tmp_time > 0:
		sql = 'select * from demo where time > %s' %(tmp_time)
	else:
		sql = 'select * from demo'

	cursor.execute(sql)

	arr = []
	values = cursor.fetchall()
	for i in values :
		arr.append([i[0],i[1],i[2],i[3]])
	if len(arr) > 0:
	    tmp_time = arr[-1][0]

	return HttpResponse(json.dumps(arr))