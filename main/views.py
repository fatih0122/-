from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    total_recipes = Recipe.objects.all().count()
    context = {
        "title":"Homepage",
        "total_recipes":total_recipes,
    }  
        
    return render(request, "home.html", context)

def search(request):
    recipes = Recipe.objects.all()

    if "search" in request.GET:
        query = request.GET.get("search")
        queryset = recipes.filter(Q(title__icontains=query))

    if request.GET.get("쌀"):
        results = recipes.filter(Q(topic__title__icontains="쌀"))
        topic = "쌀"
    elif request.GET.get("egg"):
        results = recipes.filter(Q(topic__title__icontains="egg"))
        topic="egg"
    elif request.GET.get("rice"):
        results = recipes.filter(Q(topic__title__icontains="rice"))
        topic="rice"
    elif request.GET.get("cabbage"):
        results = recipes.filter(Q(topic__title__icontains="cabbage"))
        topic="cabbage"
    elif request.GET.get("chicken"):
        results = recipes.filter(Q(topic__title__icontains="chicken"))
        topic="chicken"
    elif request.GET.get("sugar"):
        results = recipes.filter(Q(topic__title__icontains="sugar"))
        topic="sugar"
    elif request.GET.get("gouchujang"):
        results = recipes.filter(Q(topic__title__icontains="gouchujang"))
        topic="gouchujang"
    elif request.GET.get("밀"):
        results = recipes.filter(Q(topic__title__icontains="밀"))
        topic="밀"

    total = results.count()

    #paginate results
    paginator = Paginator(results, 3)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        "topic":topic,
        "page":page,
        "total":total,
        "query":query,
        "results":results,
    }
    return render(request, "search.html", context)

def detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        "recipe":recipe,
    }
    return render(request, "detail.html", context)