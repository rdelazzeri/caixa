from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Meu Caixa .feito'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
    path('', include('caixa.urls')),
   
]