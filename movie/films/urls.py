from django.contrib import admin
from django.views.generic import CreateView
from django.conf.urls.static import static
from django.urls import path
from films.views import *
from django.conf import settings
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register, name='register'),

    path('login/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),

    path('', HomeViews.as_view(), name='home'),

    path('genres/<int:genre_id>/', FilmsByGenre.as_view(), name='genres'),

    path('film/<int:id>/', film_detail_view, name='films'),

    path('sessions/today', HomeViewsByDate.as_view(), name='sessions'),

    path('sessions/1', HomeViewsByDate.as_view(inputed_number=1), name='sessions_1'),
    path('sessions/2', HomeViewsByDate.as_view(inputed_number=2), name='sessions_2'),
    path('sessions/3', HomeViewsByDate.as_view(inputed_number=3), name='sessions_3'),
    path('film/add-preference/', CreateView.as_view(form_class=FilmsForm, template_name='films/add_preference.html', success_url=reverse_lazy('home')), name='add_preference')
]


