"""
To render HTML web pages
"""

from django.http import HttpResponse
import random
from articles.models import Articles


def home_view(request):
    """
    Take in a request (Django sends request)
    Return a HTML as a response (We pick to return a response)
    """

    name = 'Boyd'
    random_id = random.randint(1, 4)
    article_obj = Articles.objects.get(id=random_id)

    H1_STRING = f"""
    <h1> {article_obj.title} (id: {article_obj.id}) ! </h1>"""

    P_STRING = f"""
    <p> {article_obj.content}</p>
    """
    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)
