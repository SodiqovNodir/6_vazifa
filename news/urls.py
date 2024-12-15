from django.urls import path


from news.views import asosiy, select, select_car

urlpatterns = [
    path('', asosiy, name="home"),
    path('brand/<int:brand_id>/', select, name='select'),
    path('car/<int:car_id>/', select_car, name='select_car'),

]