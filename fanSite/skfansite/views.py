from django.shortcuts import render, get_object_or_404
from .models import Book, Author


# Create your views here.
def home(request):
    """Renders the index page

        :param HttpRequest request:

        :returns: HttpResponse that renders the index page,

        :rtype: HttpResponse
    """
    book_list = Book.objects.order_by('-pub_date')
    author_list = Author.objects
    context = {'book_list': book_list, 'author_list': author_list}
    return render(request, 'home.html', context)


def detail(request, book_id):
    """Renders a detailed view of the selected book
    from which the user can purchase a book

        :param HttpRequest request:
        :param int book_id: the id of the selected book

        :returns: HttpResponse that renders the detail page,
        with context from the book table

        :rtype: HttpResponse
    """
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})


def author_detail(request, author_id):
    """Renders a detailed view of the selected author
    from which the user can purchase a book

        :param HttpRequest request:
        :param int author_id: the id of the selected author

        :returns: HttpResponse that renders the author page,
        with context from the author and book tables

        :rtype: HttpResponse
    """
    author = get_object_or_404(Author, pk=author_id)
    works_list = Book.objects.filter(author_id__exact=author_id)
    return render(request, 'author.html',
                  {'author': author, 'works_list': works_list})


def purchased(request):
    """Renders the purchase page

        :param HttpRequest request:

        :returns: HttpResponse that renders the purchased page,

        :rtype: HttpResponse
    """
    return render(request, 'purchased.html')
