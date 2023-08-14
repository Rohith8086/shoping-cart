from django. urls import path
from . import views

app_name='sear_app'
urlpatterns=[
    path('',views.Search,name='Search'),
]