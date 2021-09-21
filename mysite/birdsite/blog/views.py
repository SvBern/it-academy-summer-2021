from django.shortcuts import render, get_object_or_404
from .models import Category, Bird
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm


def bird_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    birds = Bird.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        birds = birds.filter(category=category)
    """
    object_list = Bird.objects.all()
    paginator = Paginator(object_list, 4)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        birds = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        birds = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        birds = paginator.page(paginator.num_pages)
    """
    return render(request,
                  'blog/bird/list.html',
                  {'category': category,
                   'categories': categories,
                   'birds': birds})


def bird_detail(request, slug):
    bird = get_object_or_404(Bird,
                             slug=slug,
                             )
    return render(request,
                  'blog/bird/detail.html',
                  {'bird': bird})


def bird_search(request):
    queue = None
    results = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Bird.objects.filter(search=query)
        return render(request, 'blog/bird/search.html', {'form': form,
                                                         'query': query,
                                                         'results': results})
