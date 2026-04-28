from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conectando as rotas
    path('materiais/', include('materiais.urls')),
<<<<<<< HEAD
=======
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
>>>>>>> f1bdbbb0b09fece83f62523247bcc05483493c58
]