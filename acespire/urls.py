from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home_page"),
    path('services/', views.products, name="products_page"),
    path('whyweare/', views.whyweare, name="whyweare_page"),
    path('research/', views.research, name="research_page"),
    path('aboutus/', views.about, name="about_page"),
    path('career/', views.career, name="career_page"),
    path('contact/', views.contact, name="contact_page"),
    path('employee/', views.employee, name="employee_page"),
]
