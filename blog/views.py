# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Article
from .forms import ArticleForm

# Guest Section
def home(request):
    try:
        articles = Article.objects.filter(
            date_published__lte=timezone.now()
        ).order_by('-date_published')
        return render(request, 'blog/home.html', {'articles': articles})
    except Exception as e:
        messages.error(request, f"Error loading articles: {str(e)}")
        return render(request, 'blog/home.html', {'articles': []})

def article_detail(request, id):
    try:
        article = get_object_or_404(Article, id=id, date_published__lte=timezone.now())
        return render(request, 'blog/article.html', {'article': article})
    except Article.DoesNotExist:
        messages.error(request, "Article not found.")
        return redirect('blog:home')

# Admin Section
@login_required(login_url='blog:login')
def dashboard(request):
    try:
        articles = Article.objects.all().order_by('-date_published')
        return render(request, 'blog/admin/dashboard.html', {'articles': articles})
    except Exception as e:
        messages.error(request, f"Error loading dashboard: {str(e)}")
        return render(request, 'blog/admin/dashboard.html', {'articles': []})

@login_required(login_url='blog:login')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            try:
                article = form.save(commit=False)
                article.date_published = timezone.now()
                article.save()
                messages.success(request, "Article created successfully!")
                return redirect('blog:dashboard')
            except Exception as e:
                messages.error(request, f"Error creating article: {str(e)}")
    else:
        form = ArticleForm()
    return render(request, 'blog/admin/form.html', {
        'form': form, 
        'action': 'Add'
    })

@login_required(login_url='blog:login')
def edit_article(request, id):
    try:
        article = get_object_or_404(Article, id=id)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.save()
                messages.success(request, "Article updated successfully!")
                return redirect('blog:dashboard')
        else:
            form = ArticleForm(instance=article)
        return render(request, 'blog/admin/form.html', {
            'form': form, 
            'action': 'Edit'
        })
    except Article.DoesNotExist:
        messages.error(request, "Article not found.")
        return redirect('blog:dashboard')

@login_required(login_url='blog:login')
def delete_article(request, id):
    try:
        article = get_object_or_404(Article, id=id)
        if request.method == 'POST':
            article.delete()
            messages.success(request, "Article deleted successfully!")
            return redirect('blog:dashboard')
        return render(request, 'blog/admin/delete_confirmation.html', {'article': article})
    except Article.DoesNotExist:
        messages.error(request, "Article not found.")
        return redirect('blog:dashboard')