from .views import TeacherView, StudentView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("teachers", TeacherView)
router.register("students", StudentView)

urlpatterns = [

]
urlpatterns += router.urls