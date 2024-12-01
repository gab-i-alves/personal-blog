# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Article

# Guest Section
def home(request):
    articles = Article.objects.filter(
        date_published__lte=timezone.now()
    ).order_by('-date_published')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id, date_published__lte=timezone.now())
    return render(request, 'blog/article.html', {'article': article})

# Admin Section
def dashboard():
    ...

def add_article():
    ...

def edit_article():
    ...

def delete_article():
    ...

