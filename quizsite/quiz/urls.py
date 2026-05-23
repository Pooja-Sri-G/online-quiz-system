from django.urls import path
from . import views

urlpatterns = [

    # Authentication
    path('', views.login_view, name ='base'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Quiz
    path('quiz/', views.quiz_view, name='quiz'),
    path('submit-quiz/', views.submit_quiz_view, name='submit_quiz'),

    # Certificate
    path('certificate/', views.certificate_view, name='certificate'),
]
