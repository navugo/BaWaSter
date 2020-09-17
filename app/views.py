from django.shortcuts import get_object_or_404, render
from .models import Record


def index(request):
    """used to display index page of application"""
    return render(request, 'app/index.html')


def records(request):
    """used to display latest transfers"""
    data = get_object_or_404(Record)
    return render(request, 'app/transfer_records.html', {'data': data})


def ballast_records(request, ballast_id):
    """used to display dedicated ballast records"""
    data = get_object_or_404(Record, pk=ballast_id)
    return render(request, 'app/ballast_records.html', {'data': data})


def about(request):
    return render(request, 'app/about.html')
