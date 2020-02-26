from django.urls import path,include
# from django.contrib.auth import views as auth_views


from quiz import views

urlpatterns = [
    path('home/<int:level_id>',views.home, name='home'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('get/<int:level_id>/', views.get_mcq, name='get_mcq'),
    path('post/<int:level_id>/<int:question_id>/', views.validate_mcq, name='validate_mcq'),
    path('signup/', views.signup, name='signup'),
]