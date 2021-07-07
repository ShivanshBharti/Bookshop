from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('show',views.show,name="show"),
    path('<int:id>',views.display,name="display"),
    path('search',views.search,name="search"),
]
