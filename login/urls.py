from django.urls import path
from . import views # import the views of current app


app_name = 'login'
urlpatterns = [
	path("", views.index, name="index"),
]