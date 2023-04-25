from django.urls import path
# from .import views
from . views import *

urlpatterns = [
    # path('browser', views.function in views.py file, # name=template),
    # path('', views.index, name='index')
    path('', index, name='index'),
    path('category/', category, name='category'),
    path('product/', product, name='product'),
    path('categories/<str:id>/', categories, name='categories'),
    # path('categories/<slug:slug>/', categories, name='categories'),
    path('details/<slug:slug>/', details, name='details'),

    path('contact/', contact, name='contact'),

    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile_update/', profile_update, name='profile_update'),
    path('password/', password, name='password'),
    path('search/', search, name='search'),

    path('shopcart/', shopcart, name='shopcart'),
    path('displaycart/', displaycart, name='displaycart'),
    path('deleteitem/', deleteitem, name='deleteitem'),
    path('change/', change, name='change'),
    path('checkout/', checkout, name='checkout'),
    path('pay/', pay, name='pay'),
    path('callback/', callback, name='callback'),
]
