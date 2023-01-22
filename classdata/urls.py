from .views import TeacherView, StudentView, LessonView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("teachers", TeacherView)
router.register("students", StudentView)
router.register("lessons", LessonView)

urlpatterns = [

]
urlpatterns += router.urls