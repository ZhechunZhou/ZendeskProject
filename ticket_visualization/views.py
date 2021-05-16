import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

from ticket_visualization.models import Ticket


def home(request):
    return render(request, 'welcome.html', {})


def update_data():
    """
    This function read from Zendesk web Api to get the Latest tickets.
    It only add new tickets and do not delete the tickets from the database,
    for the ticket list collected may not be complete.
    :param request:
    :return: updated ticket list
    """
    # list of ids of tickets in the database

    response = requests.get('https://zhechundemo.zendesk.com/api/v2/tickets.json',
                            auth=('zhechunzhou@gmail.com', 'PAi31415926'))
    tickets = response.json()['tickets']

    for ticket in tickets:
        if not Ticket.objects.filter(id=ticket['id']).exists():
            new_ticket = Ticket(id=ticket['id'], url=ticket['id'], created_at=ticket['created_at'],
                                description=ticket['description'], due_at=ticket['due_at'],
                                assignee_id=ticket['assignee_id'], requester_id=ticket['requester_id'],
                                submitter_id=ticket['submitter_id'],
                                priority=ticket['priority'], status=ticket['status'],
                                subject=ticket['subject'], type=ticket['type'],
                                updated_at=ticket['updated_at'])
            print(new_ticket)
            new_ticket.save()
        return


def get_tickets(request):
    """
    This function gets tickets from database
    :return: a list of tickets in json format
    """
    update_data()
    response_data = []
    for ticket in Ticket.objects.all():
        ticket_json = {
            'id': ticket.id,
            'assignee_id': ticket.assignee_id,
            'created_at': ticket.created_at.strftime(
                "%-m/%-d/%Y %-I:%-M %p"),
            'description': ticket.description,
            'due_at': ticket.due_at,
            'priority': ticket.priority,
            'status': ticket.status,
            'subject': ticket.subject,
            'submitter_id': ticket.submitter_id,
            'type': ticket.type,
            'updated_at': ticket.updated_at.strftime(
                "%-m/%-d/%Y %-I:%-M %p"),
            'url': ticket.url,
        }
        print(ticket_json)
        response_data.append(ticket_json)

    response_json = json.dumps(response_data)
    return HttpResponse(response_json, content_type='application/json')


def display_tickets(request):
    return render(request, 'ticket_visualization/dashboard.html', {})
