from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'errata', views.ErrataView)
router.register(r'books', views.BookView)

urlpatterns = [
    path('admin/dashboard/', views.dashboard, name='errata_dashboard'),
    path('admin/list/', views.list, name='errata_list'),
    path('admin/edit/', views.edit, name='errata_edit'),
    path('api/', include(router.urls)),
]
