from rest_framework.routers import DefaultRouter
from apps.main.views import ProductMixins, CharacteristicMixins

router = DefaultRouter()

router.register(r'products', ProductMixins, basename='product')
router.register(r'characteristics', CharacteristicMixins, basename='characteristic')


urlpatterns = router.urls

