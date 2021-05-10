from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import requests


def home(request):
    return render(request, 'welcome.html', {})


def update_data():
    response = requests.get('https://zhechundemo.zendesk.com/api/v2/problems.json',
                            auth=('{email_address}', '{password}'))
    geodata = response.json()

