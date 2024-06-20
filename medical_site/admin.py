from django.contrib import admin
from medical_site.models import Hospitals,Doctors,Products,Contact,Department,Blog

@admin.register(Hospitals)
class HospitalsAdmin(admin.ModelAdmin):
    list_display = ('pk','name','location','email')
    list_filter = ('location',)
    search_fields = ('location',)

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('pk','first_name','last_name','year_of_experience','department','hospital')
    list_filter = ('hospital','year_of_experience','department',)
    search_fields = ('hospital','year_of_experience','department',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk','name','price')
    list_filter = ('price',)
    search_fields = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','number','email')
    list_filter = ('number',)
    search_fields = ('name','number')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','description','created_at','owner')