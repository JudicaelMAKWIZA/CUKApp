
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Chemin d'accès à la page admin
    path('admin/', admin.site.urls),

    #Chemin qui mène à la page d'accueil
    path('', views.frontend, name="frontend"),

    #chemin login/logout
    path('login/', include("django.contrib.auth.urls")),

    # ===========================
    # SECTION BACKEND
    # ===========================

    #Chemin d'accès à la page backend(page de patient)
    path('backend/', views.backend, name="backend"),

    #Chemin d'ajout du patient
    path('add_patient', views.add_patient, name="add_patient")

]
