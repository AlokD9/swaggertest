from rest_framework.routers import SimpleRouter
from .views import EmpViewSet,AddressViewSet

router = SimpleRouter()
router.register("swaggerapp",EmpViewSet)
router.register("Address",AddressViewSet)

urlpatterns = router.urls
