from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Studentmodel",views.studentapi)
router.register("Marksmodel",views.marksapi)


urlpatterns = [
    path('',include(router.urls)),
    path('index',views.index,name='index'),
    path('thanks',views.thanks, name = 'thanks'),
    path('checkout',views.checkout, name = 'checkout'),
    path('stripe_webhook',views.my_webhook_view, name = 'my_webhook_view'),
]