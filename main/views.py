from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        top9_articles = Article.objects.filter(published=True).order_by('-views')[:9]
        top10_articles = Article.objects.filter(published=True).order_by('-created_at')[:10]
        context = {
            'top4_articles': Article.objects.order_by('-views')[:4],
            'top9_articles': top9_articles,
            'top10_articles': top10_articles,

        }
        return render(request, "index.html", context)

    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            Newsletter.objects.create(email=email)
        return redirect('home')


class ContactView(View):
    def get(self, request):
        # contact = Contact.objects.all()
        context = {
            # 'contact': contact

        }
        return render(request, 'contact.html', context, )
    def post(self, request):
        # contact=get_object_or_404(Contact)
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
            # contact=contact

        )
        return redirect('contact')

class ArticleDetailsView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        same_articles = Article.objects.filter(category=article.category).order_by('-created_at')[:5]
        context = {

            'article': article,

            'same_articles': same_articles,
        }
        return render(request, 'detail-page.html', context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        Comment.objects.create(
            author=request.POST.get('author'),
            email=request.POST.get('email'),
            text=request.POST.get('text'),
            article=article

        )
        return redirect('article_details', slug=slug)
