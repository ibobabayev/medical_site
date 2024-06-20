from django.urls import path
from medical_site.apps import MedicalSiteConfig
from medical_site.views import HomePageTemplateView , HospitalCreateView , HospitalListView , HospitalDetailView , HospitalUpdateView , HospitalDeleteView
from medical_site.views import DoctorsCreateView,DoctorsListView,DoctorsDetailView,DoctorsUpdateView,DoctorsDeleteView
from medical_site.views import DepartmentCreateView,DepartmentListView,DepartmentDetailView,DepartmentUpdateView,DepartmentsDeleteView
from medical_site.views import ProductsCreateView,ProductsListView,ProductsDetailView,ProductsUpdateView,ProductsDeleteView
from medical_site.views import BlogCreateView,BlogListView,BlogDetailView,BlogUpdateView,BlogDeleteView
from medical_site.views import ContactTemplateView
app_name = MedicalSiteConfig.name

urlpatterns = [
    path('',HomePageTemplateView.as_view(),name='home'),
    path('hospital_add/',HospitalCreateView.as_view(),name='add_hospital'),
    path('hospital_list/',HospitalListView.as_view(),name='list_hospital'),
    path('hospital_view/<int:pk>',HospitalDetailView.as_view(),name='view_hospital'),
    path('hospital_edit/<int:pk>',HospitalUpdateView.as_view(),name='edit_hospital'),
    path('hospital_delete/<int:pk>',HospitalDeleteView.as_view(),name='delete_hospital'),
    path('doctor_add/', DoctorsCreateView.as_view(), name='add_doctor'),
    path('doctor_list/', DoctorsListView.as_view(), name='list_doctor'),
    path('doctor_view/<int:pk>', DoctorsDetailView.as_view(), name='view_doctor'),
    path('doctor_edit/<int:pk>', DoctorsUpdateView.as_view(), name='edit_doctor'),
    path('doctor_delete/<int:pk>', DoctorsDeleteView.as_view(), name='delete_doctor'),
    path('department_add/', DepartmentCreateView.as_view(), name='add_department'),
    path('department_list/', DepartmentListView.as_view(), name='list_department'),
    path('department_view/<int:pk>', DepartmentDetailView.as_view(), name='view_department'),
    path('department_edit/<int:pk>', DepartmentUpdateView.as_view(), name='edit_department'),
    path('department_delete/<int:pk>', DepartmentsDeleteView.as_view(), name='delete_department'),
    path('product_add/', ProductsCreateView.as_view(), name='add_product'),
    path('product_list/', ProductsListView.as_view(), name='list_product'),
    path('product_view/<int:pk>', ProductsDetailView.as_view(), name='view_product'),
    path('product_edit/<int:pk>', ProductsUpdateView.as_view(), name='edit_product'),
    path('product_delete/<int:pk>', ProductsDeleteView.as_view(), name='delete_product'),
    path('blog_add/', BlogCreateView.as_view(), name='add_blog'),
    path('blog_list/', BlogListView.as_view(), name='list_blog'),
    path('blog_view/<int:pk>', BlogDetailView.as_view(), name='view_blog'),
    path('blog_edit/<int:pk>', BlogUpdateView.as_view(), name='edit_blog'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
]