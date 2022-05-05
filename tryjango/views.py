"""
To render HTML web pages
"""

from django.template.loader import render_to_string
from django.http import HttpResponse
import random
from articles.models import Articles


def article_home_view(request):
    return HttpResponse


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return a HTML as a response (We pick to return a response)
    """

    name = 'Boyd'
    random_id = random.randint(1, 4)
    article_obj = Articles.objects.get(id=random_id)
    article_queryset = Articles.objects.all()

    context = {
        'object_list': article_queryset,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }

    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING = """
    #     <h1> {title} (id: {id})!</h1>
    #     <p> {content}!</p>
    #     """.format(**context)

    return HttpResponse(HTML_STRING)
