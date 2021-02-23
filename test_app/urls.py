from django.urls import path,include
from . import views
from serializers_2_project import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.list_data.as_view(),name = 'list_data'),
    path('newpage',views.newpage.as_view(),name = 'newpage'),
    path('forupdate/<str:pk>',views.forupdate.as_view(),name = 'forupdate'),
    path('serial_test',views.serial_test.as_view(),name = 'serial_test'),
    path('ajaxpage',views.ajaxpage,name='ajaxpage'),
    path('create_profile',views.create_profile.as_view(), name='create_profile'),
    path('<str:pk>',views.list_update_data.as_view(), name = 'list_update_data'),
    path('data_list/',views.new_details_page.as_view(),name='new_details_page'),
    path('customer_form/',views.customer_form.as_view(), name='customer_form'),
    
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
