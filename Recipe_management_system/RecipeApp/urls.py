from django.urls import path
from RecipeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('sign_up', sign_up, name='sign_up'),
    path('login', sign_in, name='sign_in'),
    path("logout", logout_view, name="logout"),
    path('profile', profile, name='profile'),
    path('change_pass', change_pass, name='change_pass'),
    path('all_recipe', all_recipe, name='all_recipe'),
    path('blog', blog, name='blog'),
    path('contract', contact, name='contact')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)