
from django.contrib import admin
from django.urls import path
from Inventory.views import listar_productos, eliminar_productos, agregar_productos


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/", admin.site.urls),
    

]
