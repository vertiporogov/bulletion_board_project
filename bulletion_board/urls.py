from bulletion_board.apps import BulletionBoardConfig
from django.urls import path

from bulletion_board.views import AdsCreateAPIView, AdsListAPIView, AdsRetrieveAPIView, AdsUpdateAPIView, \
    AdsDestroyAPIView, FeedbackCreateAPIView, FeedbackListAPIView, FeedbackRetrieveAPIView, FeedbackUpdateAPIView, \
    FeedbackDestroyAPIView

app_name = BulletionBoardConfig.name

urlpatterns = [
    path('create/', AdsCreateAPIView.as_view(), name='create_ad'),
    path('list/', AdsListAPIView.as_view(), name='list_ad'),
    path('detail/<int:pk>/', AdsRetrieveAPIView.as_view(), name='detail_ad'),
    path('update/<int:pk>/', AdsUpdateAPIView.as_view(), name='update_ad'),
    path('delete/<int:pk>/', AdsDestroyAPIView.as_view(), name='delete_ad'),

    path('create/feetback/', FeedbackCreateAPIView.as_view(), name='create_feedback'),
    path('list/feetback/', FeedbackListAPIView.as_view(), name='list_feedback'),
    path('detail/feetback/<int:pk>/', FeedbackRetrieveAPIView.as_view(), name='detail_feedback'),
    path('update/feetback/<int:pk>/', FeedbackUpdateAPIView.as_view(), name='update_feedback'),
    path('delete/feetback/<int:pk>/', FeedbackDestroyAPIView.as_view(), name='delete_feedback'),
]
