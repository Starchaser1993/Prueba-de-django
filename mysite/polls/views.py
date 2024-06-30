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
    # Obtener las noticias de NASA y The Astrophysical Journal Letters
    nasa_news = scrape_nasa()
    journal_news = scrape_astrophysical_journal_letters()
    
    # Pasar los datos al contexto de renderización
    context = {
        'nasa_news': nasa_news,
        'journal_news': journal_news,
    }
    
    return render(request, 'polls/show_cosmic_news.html', context)


