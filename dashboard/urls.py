from django.urls import path
from . import views # import the views of current app


app_name = 'dashboard'
urlpatterns = [
	path("", views.index, name="index"), # attach index view to "index" url
	path("domains/", views.domains, name="domains"),
	path("scope/", views.scope, name="scope"),
	path("gitdorks/", views.githubdorks, name='gitdorks'),
	path("ggdorks/", views.googledorks, name='ggdorks'),
	path("acquisitions/", views.acquisitions, name='acquisitions'),
	path("methodology/", views.methodology, name='methodology'),
	path("mynotes/", views.myNotes, name='myNotes'),
	path("profile/", views.profile, name='profile'),
	path("logout/", views.logout_user, name='logout'),
]