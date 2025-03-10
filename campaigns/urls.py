from django.urls import path
from .views import HotmartProductsView, HotmartSalesView, ChatGPTView, index, CampaignCreateView

urlpatterns = [
    path('hotmart/products/', HotmartProductsView.as_view(), name='hotmart-products'),
    path('hotmart/sales/', HotmartSalesView.as_view(), name='hotmart-sales'),
    path('chatgpt/generate/', ChatGPTView.as_view(), name='chatgpt-generate'),
    path('', index, name='index'),
    path('create/', CampaignCreateView.as_view(), name='create-campaign'),

]
