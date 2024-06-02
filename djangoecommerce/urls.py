from django.contrib import admin
from django.urls import include, path
from core import views as core_views
from catalog import views as catalog_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('contato/', core_views.contact, name='contact'),
    path('produto/', core_views.product, name='product'),
    path('produtos/', include(('catalog.urls', 'catalog'), namespace='catalog')),

    path('admin/', admin.site.urls),
]
