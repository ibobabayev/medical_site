from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy

from medical_site.models import Hospitals,Doctors,Department,Products,Blog,Contact
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,TemplateView

from pytils.translit import slugify

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
class HomePageTemplateView(TemplateView):
    template_name = 'medical_site/base.html'
class HospitalCreateView(LoginRequiredMixin,CreateView):
    model = Hospitals
    login_url = "users:login"
    fields = "__all__"
    success_url = reverse_lazy('medical_site:list_hospital')

class HospitalListView(ListView):
    model = Hospitals

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['hospital_list'] = Hospitals.objects.all()
        return context_data


class HospitalDetailView(LoginRequiredMixin,DetailView):
    model = Hospitals
    login_url = "users:login"
    extra_context = {'hospital_list': Hospitals.objects.all()}

class HospitalUpdateView(LoginRequiredMixin,UpdateView):
    model = Hospitals
    login_url = "users:login"
    fields = ("name","description","location","preview","email")
    success_url = reverse_lazy('medical_site:list_hospital')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404

class HospitalDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Hospitals
    login_url = "users:login"
    success_url = reverse_lazy('medical_site:list_hospital')

    def test_func(self):
        return self.request.user.is_staff
class DoctorsCreateView(LoginRequiredMixin,CreateView):
    model = Doctors
    login_url = "users:login"
    fields = "__all__"
    success_url = reverse_lazy('medical_site:list_doctor')

class DoctorsListView(ListView):
    model = Doctors
    extra_context = {'doctors_list': Doctors.objects.all()}

class DoctorsDetailView(LoginRequiredMixin,DetailView):
    model = Doctors
    login_url = "users:login"
    extra_context = {'doctors_list': Doctors.objects.all()}

class DoctorsUpdateView(LoginRequiredMixin,UpdateView):
    model = Doctors
    login_url = "users:login"
    fields = ("avatar","year_of_experience","hospital","department",)
    success_url = reverse_lazy('medical_site:list_doctor')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404
class DoctorsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Doctors
    login_url = "users:login"
    success_url = reverse_lazy('medical_site:list_doctor')

    def test_func(self):
        return self.request.user.is_staff

class DepartmentCreateView(LoginRequiredMixin,CreateView):
    model = Department
    login_url = "users:login"
    fields = "__all__"
    success_url = reverse_lazy('medical_site:list_department')

class DepartmentListView(ListView):
    model = Department
    extra_context = {'department_list': Department.objects.all()}

class DepartmentDetailView(LoginRequiredMixin,DetailView):
    model = Department
    login_url = "users:login"
    extra_context =  {'department_list': Department.objects.all()}

class DepartmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Department
    login_url = "users:login"
    fields = ("name","description",)
    success_url = reverse_lazy('medical_site:list_department')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404

class DepartmentsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Department
    login_url = "users:login"
    success_url = reverse_lazy('medical_site:list_department')

    def test_func(self):
        return self.request.user.is_staff
class ProductsCreateView(LoginRequiredMixin,CreateView):
    model = Products
    login_url = "users:login"
    fields = "__all__"
    success_url = reverse_lazy('medical_site:list_product')

class ProductsListView(ListView):
    model = Products
    extra_context = {'product_list': Products.objects.all()}

class ProductsDetailView(LoginRequiredMixin,DetailView):
    model = Products
    login_url = "users:login"
    extra_context =   {'product_list': Products.objects.all()}

class ProductsUpdateView(LoginRequiredMixin,UpdateView):
    model = Products
    login_url = "users:login"
    fields = ("name","description","price","photo")
    success_url = reverse_lazy('medical_site:list_product')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404

class ProductsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Products
    login_url = "users:login"
    success_url =reverse_lazy('medical_site:list_product')

    def test_func(self):
        return self.request.user.is_staff
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    login_url = "users:login"
    fields = ("name","description","preview",)
    success_url = reverse_lazy('medical_site:list_blog')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)

class BlogListView(ListView):
    model = Blog
    extra_context = {'blog_list': Blog.objects.all()}

class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Blog
    login_url = "users:login"
    extra_context = {'blog_list': Blog.objects.all()}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    login_url = "users:login"
    fields = ("name","description","preview",)
    success_url = reverse_lazy('medical_site:list_blog')

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner == self.request.user or self.request.user.is_superuser:
            return self.object
        else:
            raise Http404

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    login_url = "users:login"
    success_url =reverse_lazy('medical_site:list_blog')

    def test_func(self):
        return self.request.user.is_staff

class ContactTemplateView(TemplateView):
    template_name = 'medical_site/contact.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        contact_info = Contact.objects.all()
        context_data['contact_book'] = contact_info
        return context_data

    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя:{name} , номер телефона:{phone} , сообщение: {message}')
        return render(request,self.template_name)
