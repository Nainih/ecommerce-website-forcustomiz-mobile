
from django.urls import path

from napp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create_account/',views.create_account,name='create_account'),
    path('login',views.handel_login,name='login'),
    path('custamization/',views.select_custamization,name='custamization'),
    path('logout/',views.logout_view,name='logout'),
    path('kart',views.kart,name='kart'),
    path('ordered',views.ordered,name='ordered'),
    path('brand/',views.brand,name='brand'),
    path('screen/',views.screen,name='screen'),
    path('processor/',views.processor,name='processor'),
    path('ram/',views.ram,name='ram'),
    path('camera/',views.camera,name='camera'),
    path('log',views.log,name='log'),
    path('buy',views.Buy,name='buy'),
   
]

   
    
   
