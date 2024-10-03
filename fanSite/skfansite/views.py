from django.shortcuts import render, get_object_or_404
from .models import Book, Author


# Create your views here.
def home(request):
    '''Renders the home page and passes a dict
      containing all the authors and books'''
    book_list = Book.objects.order_by('-pub_date')
    author_list = Author.objects
    context = {'book_list': book_list, 'author_list': author_list}
    return render(request, 'home.html', context)


def detail(request, book_id):
    '''Returns a detailed view of the selected book

    Args:
    -book_id: the id of the selected book'''
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


def author_detail(request, author_id):
    '''Returns a detailed view of the author, with their bio and works

    Args:
    -author_id: the id of the selected author'''
    author = get_object_or_404(Author, pk=author_id)
    works_list = Book.objects.filter(author_id__exact=author_id)
    return render(request, 'author.html',
                  {'author': author, 'works_list': works_list})


def purchased(request):
    '''Renders the successful purchase page'''
    return render(request, 'purchased.html')
