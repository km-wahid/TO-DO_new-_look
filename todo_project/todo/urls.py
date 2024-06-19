from . import views
from django.urls import path
from . views import TaskList, Detail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, Registration,TaskReorder
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", Detail.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    path("login/", CustomLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", Registration.as_view(), name="Registration"),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]

