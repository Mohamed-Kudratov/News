from django.shortcuts import render

from news.models import NewsModel, CategoryModel


def index(request):
    news = NewsModel.objects.order_by('-pk')

    q = request.GET.get('q')
    if q:
        news = news.filter(title__icontains=q)

    category = request.GET.get('category')
    if category:
        news = news.filter(category__id=category)
    category = CategoryModel.objects.all()
    context = {
        'category': category,
        'data': news
    }
    return render(request, 'home/index.html', context)
