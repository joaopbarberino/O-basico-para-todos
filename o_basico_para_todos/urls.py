"""o_basico_para_todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_principal import views
from django.conf.urls import url

urlpatterns = [
    path('', views.pagina_inicial),
    path('consulta', views.ExibirLivro.as_view()),
    path('admin/', admin.site.urls),
    path('ajuda', views.ajuda),
    url(r'^contato/$', views.email, name = 'sendmail'),
    url(r'^cadastro/$', views.cadastro_usuario, name = 'signup'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
