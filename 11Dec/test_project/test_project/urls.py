"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path#,re_path, include
from hello import views

# product_patterns = [
#     path("", views.products),
#     # path("new", views.new),
#     # path("top", views.top),
#     path("comments", views.comments),
#     path("questions", views.questions),

# ]
    

urlpatterns = [
    
    # re_path(r'^about/contact', views.about),
    # re_path(r'^about', views.about),
    path('', views.index),
    # path('about', views.about, kwargs={"name":" KOUR.IO", "age": 18}),
    # path('contact',views.contact),
    # path("products/<int:id>/", include(product_patterns))
    # path("user/", views.user)
    # path("about/", views.about),
    # path("contact/", views.contact),
    # path("details/", views.details),
    # path("index/<int:id>", views.index),
    # path("access/<int:age>", views.access)
    # path("set", views.set),
    # path("get", views.get),

]


