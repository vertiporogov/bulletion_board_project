from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from bulletion_board.models import Ad, Feedback
from bulletion_board.paginations import AdPagination
from bulletion_board.permissions import IsOwner, IsAdmin
from bulletion_board.serializers import AdSerializer, FeedbackSerializer


class AdsCreateAPIView(CreateAPIView):
    """
    Контроллер для создания объявлерния
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdsListAPIView(ListAPIView):
    """
    Контроллер для вывода списка объявлений
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('title',)


class AdsRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для вывода объявления
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdsUpdateAPIView(UpdateAPIView):
    """
    Контроллер для изменения объявления
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]


class AdsDestroyAPIView(DestroyAPIView):
    """
    Контроллер для удаления объявления
    """
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]


class FeedbackCreateAPIView(CreateAPIView):
    """
    Контроллер для создания комментария
    """
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeedbackListAPIView(ListAPIView):
    """
    Контроллер для вывода списка комментариев
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]


class FeedbackRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для вывода комментариев
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    # permission_classes = [IsAuthenticated]


class FeedbackUpdateAPIView(UpdateAPIView):
    """
    Контроллер для изменения комментария
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]


class FeedbackDestroyAPIView(DestroyAPIView):
    """
    Контроллер для удаления комментария
    """
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
