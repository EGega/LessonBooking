from .views import TeacherView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("teachers", TeacherView)

urlpatterns = [

]
urlpatterns += router.urls