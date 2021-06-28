from django.urls import path
from . import views

app_name = 'outages'

urlpatterns = [

    path('', views.OutageListView.as_view(), name='all'),
    path('active/', views.OutageActiveListView.as_view(), name='active-outages'),
    path('pending/', views.OutagePendingListView.as_view(), name='pending'),
    path('resolved/', views.OutageResolvedListView.as_view(), name='resolved'),
    path('closed/', views.OutageClosedListView.as_view(), name='closed'),
    # path('detail/', views.py.OutageDetailView.as_view(), name='outage-detail'),
    path('<int:pk>/', views.OutageDetailView.as_view(), name='outage-detail'),
    path('<str:slug>', views.OutageDetailView.as_view(), name='outage-detail'),
    # path('update/', views.py.OutageUpdateView.as_view(), name='update'),
    # path('delete/', views.py.OutageDeleteView.as_view(), name='delete'),
]
