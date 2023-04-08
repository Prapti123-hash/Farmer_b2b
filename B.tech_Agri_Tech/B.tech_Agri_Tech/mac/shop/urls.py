from django.contrib import admin
from django.urls import path
from . import views
from .views.index import Index,contact,contact_form,stuble
from .views.signup import Signup,accountSuccess
from .views.login import Login,logout
from .views.farmer import Farmers , addStuble,stubbles_formadd, stubbles_form,viewStuble,updateStubble,updateAddStuble,deleteStuble,toolsRequired,tools_form,wallet,contactfarmer,contact_formfarmer
from .views.buyer import Buyer,provideTools,provide_tools,payment,payment_done,buyerView,buyNow,home
from .views.about import About
from .middlewares.auth import  auth_middleware
urlpatterns = [
    path('',Index.as_view(), name='Home'),
    path('contact/',contact,name="contact"),
    path('contact_form/',contact_form,name="contact_form"),
    path('stuble/',stuble,name="stuble"),
    
    
    path('signup/',Signup.as_view(),name='signup'),
    
    path('signup/login/',Login.as_view(),name='login'),
    
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    

    path('farmer/<id>/',Farmers.as_view(), name='farmer'),
    path('farmer/<id>/addStuble/', addStuble, name='addStuble'),
    path('farmer/stubbles_form/<id>', stubbles_form, name='stubbles_form'),
    path('farmer/<id>/viewStuble/',viewStuble,name="viewStuble"),
    path('farmer/updateStubble/<id>',updateStubble,name="updateStubble"),
    path('farmer/updateAddStuble/<id>',updateAddStuble,name="updateAddStubble"),
    path('farmer/deleteStuble/<id>',deleteStuble, name="deleteStuble"),
    path('farmer/<id>/toolsRequired',toolsRequired,name="toolsRequired"),
    path("farmer/<id>tools_form/",tools_form,name="tools_form"),
    path('farmer/wallet/<id>',wallet,name="wallet"),
    path('farmer/<id>/contact/',contactfarmer,name="contactfarmer"),
    path('farmer/<id>/contact_form',contact_formfarmer,name="contact_formfarmer"),

    path('buyer/',Buyer.as_view(), name='buyer'),
    path('buyer/provideTools/',provideTools,name="provideTools"),
    path('buyer/provide_tools/',provide_tools,name="provide_tools"),
    path('buyer/buyerView/', buyerView, name="buyerView"),
    path('buyer/buyNow/<id>',buyNow,name="buyNow"),
    path('buyer/payment_done/', payment_done, name="payment_done"),
    path('buyer/payment_done/home', home, name="home"),
     path('buyer/payment_done/logout', logout, name="logout"),
    path('about/',About.as_view(),name='About'),
    path('buyer/contact/',contact,name="contact"),
    path('buyer/contact_form',contact_form,name="contact_form"),
    
    path('farmer/contact/',contact,name="contact"),
        
    path('viewStuble/',viewStuble,name="viewStuble"),
    path('farmer/addStuble/addStuble/', addStuble, name='addStuble'),
    path('farmer/addStuble/viewStuble/',viewStuble,name="viewStuble"),
    path('buyer/buyerView/buyerView', buyerView, name="buyerView"),
    path('buyer/buyerView/provideTools/',provideTools,name="provideTools"),
    path('buyer/buyerView/provide_tools/',provide_tools,name="provide_tools"),
    path('buyer/buyerView/contact/',contact,name="contact"),
    path('buyer/buyerView/about/',About.as_view(),name="About"),
    
    path('buyer/contact/',contact,name="contact"),
    path('buyer/about/',About.as_view(),name="About"),
    
    path('addStuble/farmer/',Farmers.as_view,name='farmer'),
     path('farmer/provideTools/',provideTools,name="provideTools"),
     path('farmer/buyerView',buyerView, name="buyerView"),
    
     path('farmer/updateStuble/viewStuble',viewStuble,name="viewStuble"),
]