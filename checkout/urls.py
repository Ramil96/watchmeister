from django.urls import path
from . import views
from .webhooks import webhook
from .views import feedback_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/thanks/', views.feedback_thanks, name='feedback_thanks'),
]