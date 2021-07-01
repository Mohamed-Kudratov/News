from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from news.forms import NewsModelForm
from news.models import NewsModel


class NewsListView(ListView):
    # data variable -object_list
    template_name = "my_admin/index.html"

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q:
            news = NewsModel.objects.filter(title__icontains=q
                                            ).order_by('-pk')
        else:
            news = NewsModel.objects.all()
        return news


class NewsCreateView(CreateView):
    # name of form variable is  -  form
    template_name = 'my_admin/form.html'
    form_class = NewsModelForm
    success_url = '/news/'


class NewsDetailView(DetailView):
    # name of book object is - object
    template_name = 'my_admin/detail.html'
    model = NewsModel


class NewsUpdateView(UpdateView):
    template_name = 'my_admin/form.html'
    form_class = NewsModelForm
    success_url = '/news/'
    model = NewsModel
    context_object_name = 'update'


class NewsDeleteView(DeleteView):
    model = NewsModel
    success_url = '/news/'
