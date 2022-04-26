"""
To render HTML web pages
"""

from django.http import HttpResponse
import random



def home_view(request):
    """
    Take in a request (Django sends request)
    Return a HTML as a response (We pick to return a response)
    """

    name = 'Boyd'
    number = random.randint(0,100)

    H1_STRING = f"""
    <h1> Hello {name}! </h1>"""

    P_STRING = f"""
    <p> Today lucky number is: '{number}'</p>
    """
    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)
