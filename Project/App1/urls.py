from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("view-all",views.view_all,name="view-all"),
    path("add-employee",views.add_emp,name="add"),
    path("remove-employee",views.remove_emp,name="remove"),
    path("remove-employee/<int:id>",views.remove,name="remove-int"),
    path("filter-employee",views.filte_emp,name="filter")
]
