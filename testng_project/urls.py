from django.contrib import admin
from django.urls import path

from items import views as items_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', items_views.get_session_id_view),
    path('item/<int:item_id>/', items_views.get_item_card_view),
]
