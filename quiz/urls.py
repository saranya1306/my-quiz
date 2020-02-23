from django.urls import path,include

from quiz import views

urlpatterns = [
    path('',views.home, name='home'),
    path('get/<int:level_num>/', views.get_mcq, name='get_mcq'),
    path('post/<int:question_id>/', views.validate_mcq, name='validate_mcq'),
]