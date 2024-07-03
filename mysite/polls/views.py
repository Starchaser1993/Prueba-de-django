import csv
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.urls import reverse
from .scraper import scrape_nasa, scrape_astrophysical_journal_letters

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def show_cosmic_news(request):
    
    nasa_news = scrape_nasa()
    journal_news = scrape_astrophysical_journal_letters()
    
    
    context = {
        'nasa_news': nasa_news,
        'journal_news': journal_news,
    }
    
    return render(request, 'polls/show_cosmic_news.html', context)

def read_csv(request, file_type):
    
    if file_type == 'train':
        csv_file_path = os.path.join(settings.BASE_DIR, 'polls', 'data', 'pulsar_data_train.csv')
    elif file_type == 'test':
        csv_file_path = os.path.join(settings.BASE_DIR, 'polls', 'data', 'pulsar_data_test.csv')
    else:
        return HttpResponse("Invalid file type.")

    data = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = next(csvreader)
        for row in csvreader:
            data.append(row)

    context = {
        'header': header,
        'data': data,
        'file_type': file_type
    }
    return render(request, 'polls/show_csv.html', context)

def show_csv(request):
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'pulsar_data_test.csv')
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_data = list(csv_reader)

    return render(request, 'polls/show_csv.html', {'csv_data': csv_data})

def show_csv(request):
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'pulsar_data_train.csv')
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_data = list(csv_reader)

    return render(request, 'polls/show_csv.html', {'csv_data': csv_data})