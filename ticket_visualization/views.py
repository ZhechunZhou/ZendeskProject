from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie

from ticket_visualization.models import Ticket

import json
import requests


def home(request):
    return render(request, 'welcome.html', {})


def update_data():
    response = requests.get('https://zhechundemo.zendesk.com/api/v2/tickets.json',
                            auth=('zhechunzhou@gmail.com', 'PAi31415926'))
    print(response.json())


def get_tickets():
    """
    This function gets tickets from database
    :return: a list of tickets in json format
    """
    response_data = []
    for ticket in Ticket.objects.all():
        ticket_json = {
            'id': ticket.id,
            'assignee_id': ticket.assignee_id,
            'created_at': ticket.created_at,
            'description': ticket.description,
            'due_at': ticket.due_at,
            'priority': ticket.priority,
            'status': ticket.status,
            'subject': ticket.subject,
            'submitter_id': ticket.submitter_id,
            'type': ticket.type,
            'updated_at': ticket.updated_at,
            'url': ticket.url,
        }
        response_data.append(ticket_json)

    response_json = json.dumps(response_data)
    return HttpResponse(response_json, content_type='application/json')


def display_tickets(request):
    update_data()
    return render(request, 'welcome.html', {})
