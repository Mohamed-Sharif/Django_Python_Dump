from django.urls import path
from . import views

app_name = 'departments'

urlpatterns = [
    # department list view
    path('', views.DepartmentListView.as_view(), name='department_list'),
    # department detail view
    path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    # department create view
    path('create/', views.DepartmentCreateView.as_view(), name='department_create'),
    # department update view
    path('<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    # department delete view
    path('<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
]
