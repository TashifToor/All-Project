
from gymm import views

from django.urls import path,include

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.home,name='home'),
    path('About Us',views.AboutUs,name='About Us'),
    path('Join Us',views.JoinUs,name='Join Us'),
    path('Pricing',views.Pricing,name='Pricing'),
    path('Personal Trainer',views.PersonalTrainer,name='Personal Trainer'),
    path('Corporate Plans',views.CorporatePlans,name='Corporate Plans'),
    path('Membership',views.Membership,name='Membership'),
    path('Classes',views.Classes,name='Classes'),
    path('Trainers',views.Trainers,name='Trainers'),
    path('Gallery',views.Gallery,name='Gallery'),
    path('Contact Us',views.ContactUs,name='Contact Us'),
    path('Special Offers',views.SpecialOffers,name='Special Offers'),


]
