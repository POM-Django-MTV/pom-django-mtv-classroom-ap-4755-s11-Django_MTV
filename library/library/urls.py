"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
    <h1>Library</h1>
    <ul>
        <li><a href="/author/">Author</a></li>
        <li><a href="/book/">Book</a></li>

    </ul>
    """)


#  TODO: will add to home when order and user apps are implemented
# <li><a href="/order/">Order</a></li>
# <li><a href="/user/">User</a></li>


urlpatterns = [
    path("", home),
    path("author/", include("author.urls")),
    path("book/", include("book.urls")),
    # path('order/', include('order.urls')),
    # path('user/', include('user.urls')),
]
