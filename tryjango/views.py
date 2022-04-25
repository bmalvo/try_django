"""
To render HTML web pages
"""

from django.http import HttpResponse


HTML_STRING = """
<h1> Hello World! </h1>
"""


def home_view(request):
    """
    Take in a request (Django sends request)
    Return a HTML as a response (We pick to return a response)
    """
    print('Stefka piękny kot')
    return HttpResponse(HTML_STRING)
