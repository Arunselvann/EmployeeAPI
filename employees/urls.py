from rest_framework_mongoengine import routers
from employees.views import EmployeesView

router = routers.DefaultRouter()
router.register(r'employees', EmployeesView)

urlpatterns = []
urlpatterns += router.urls
