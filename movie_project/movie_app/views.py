from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from movie_app.forms import MovieForm
from movie_app.models import Movies, Category


# Create your views here.
# def index(request):
#     movies = Movies.objects.all()
#     categories = Category.objects.all()
#     items_by_category = {}
#
#     for category in categories:
#         items_by_category[category] = Movies.objects.filter(category=category)
#     return render(request, 'menu.html', {'movie': movies,'items_by_category': items_by_category})
#
#
def detail(request, id):
    movie = Movies.objects.get(id=id)
    return render(request, 'about.html', {'movies': movie})


# views.py





def index(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies=Movies.objects.all().filter(category=c_page,)
    else:
        movies=Movies.objects.all().filter()

    return render(request,'menu.html',{'category':c_page,'movies': movies})

def update(request,id):
    movies = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movies': movies})


def delete(request,id):
    if request.method =="POST":
        movies=Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')

# def add_movie(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         year = request.POST.get('year')
#         links = request.POST.get('links')
#         poster = request.FILES['poster']
#         actors=request.POST.get('actors')
#         category=request.POST.get('category')
#         movies = Movies(title=title, description=description, year=year, links=links, poster=poster,actors=actors,category=category)
#
#         movies.save()
#
#         return redirect('/')
#     return render(request, "add.html")
#
# def add_movie(request):
#     if request.method == ('POST' or None):
#         form = MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("yes")
#
#             return redirect('/')
#
#     else:
#         print("not")
#         form = MovieForm()
#
#     return render(request, 'add.html', {'form': form})



def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
        
            if 'poster' in request.FILES:
                
                # ...
                form.save()
                return HttpResponseRedirect('/')  # Redirect to success page

            else:
                #  an error 
                form.add_error('poster', 'Poster is required.')
        form.save()
    else:
        form = MovieForm()

    return render(request, 'add.html', {'form': form})
