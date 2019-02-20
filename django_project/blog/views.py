from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author': 'Aniket',
        'title': 'Blog post1',
        'content': 'xyz',
        'date_posted': 'February 18, 2019'

    },
    {
        'author': 'Aniket',
        'title': 'Blog post2',
        'content': 'xyz',
        'date_posted': 'February 18, 2019'

    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
