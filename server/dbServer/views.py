from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    cursor = connection.cursor()

    print('lolKEKcheburek')

    cursor.callproc('[dbo].[add_user]', ['tesst', 'tst_nick', 'password', '11-11-2011'])

    return HttpResponse()
