#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#UTIL
import json

from django.conf import settings

def testview(request):

    return render(request,'testview/testview.html')
