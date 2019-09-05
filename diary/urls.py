from django.urls import path

from . import views
from diary.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('write/', views.WriteView.as_view(), name = 'write'),
    path('read/', views.ReadView.as_view(), name = 'read'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('password/', views.ChangePasswordView.as_view(), name = 'password'),
    path('manage/', views.ManageEntriesView.as_view(), name = "manage"),
    path('<int:pk>/delete/', views.DeleteEntryView.as_view(), name = "deleteentry"),
]
