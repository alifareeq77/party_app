
from rest_framework import routers

from .views import PartyRoomView, PartyViewSet

router = routers.SimpleRouter()
router.register(r'party_generate', PartyViewSet, basename='party_generate')
router.register(r'party', PartyRoomView, basename='party')

urlpatterns = [] + router.urls
