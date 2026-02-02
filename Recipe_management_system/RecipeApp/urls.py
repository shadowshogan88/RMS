from django.urls import path, re_path
from RecipeApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^sign_up/?$', sign_up, name='sign_up'),
    re_path(r'^login/?$', sign_in, name='sign_in'),
    re_path(r'^logout/?$', logout_view, name='logout'),
    re_path(r'^profile/?$', profile, name='profile'),
    re_path(r'^change_pass/?$', change_pass, name='change_pass'),
    re_path(r'^all_recipe/?$', all_recipe, name='all_recipe'),
    re_path(r'^blog/?$', blog, name='blog'),
    re_path(r'^contract/?$', contact, name='contact'),
    re_path(r'^categories/?$', category_list, name='category_list'),
    re_path(r'^submit_recipe/?$', submit_recipe, name='submit_recipe')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
