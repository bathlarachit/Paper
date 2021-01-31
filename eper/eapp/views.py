from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from eapp import models
from eapp import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
class Home(TemplateView):
    template_name='eapp/base.html'

class Category(LoginRequiredMixin,CreateView):
    template_name='eapp/cat.html'
    model=models.Courses
    fields=('title',)
    login_url=reverse_lazy('login')
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.faculty=self.request.user
        return super(Category,self).form_valid(form)
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name='eapp/signup.html'
    success_url=reverse_lazy('login')
class Examlist(LoginRequiredMixin,ListView):
    template_name='eapp/exam_list.html'
    context_object_name='exam_list'
    model=models.Exam
    def get_queryset(self):
        qs=super(Examlist,self).get_queryset()
        return qs.filter(course__exact=self.kwargs['id'])

@login_required
def examlist(request,id):
    qs=models.Exam.objects.filter(course_id=id)
    return render(request,'eapp/exam_list.html',{'exam_list':qs,'pk':id})
class Exam(LoginRequiredMixin,CreateView):
    template_name='eapp/create_exam.html'
    fields=('title','total_marks','start_time','end_time')
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')
    model=models.Exam
    def form_valid(self,form):
        form.instance.course_id=self.kwargs['pk']
        return super(Exam,self).form_valid(form)
class Catlist(LoginRequiredMixin,ListView):
    context_object_name='catlist'
    template_name='eapp/cat_list.html'
    model=models.Courses
    def get_queryset(self):
        qs=super(Catlist,self).get_queryset()
        return qs.filter(faculty__exact=self.request.user)

@login_required
def question(request,pk):
    try:
        tf=models.TF.objects.filter(exam_id=pk)
    except:pass
    try:
        dis=models.discriptive.objects.filter(exam_id=pk)
    except:pass
    try:
        fill=models.fillnblanks.objects.filter(exam_id=pk)
    except:pass
    return render(request,'eapp/q_list.html',{'tf':tf,'pk':pk,'dis':dis,'fill':fill})

class TFV(LoginRequiredMixin,CreateView):
    model=models.TF
    template_name='eapp/tf.html'
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')
    fields=('question','ans','marks')
    def form_valid(self,form):
        form.instance.exam_id=self.kwargs['pk']
        return super(TFV,self).form_valid(form)
class DisV(LoginRequiredMixin,CreateView):
    model=models.discriptive
    template_name='eapp/tf.html'
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')
    fields=('question','marks')
    def form_valid(self,form):
        form.instance.exam_id=self.kwargs['pk']
        return super(DisV,self).form_valid(form)
class fillV(LoginRequiredMixin,CreateView):
    model=models.fillnblanks
    template_name='eapp/tf.html'
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')
    fields=('question','marks')
    def form_valid(self,form):
        form.instance.exam_id=self.kwargs['pk']
        return super(fillV,self).form_valid(form)
class CourseEnroll(LoginRequiredMixin,CreateView):
    model=models.studentCourses
    template_name='eapp/cour.html'
    login_url=reverse_lazy('login')
    success_url=reverse_lazy('home')
    fields=('courses',)
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(CourseEnroll,self).form_valid(form)
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser
class Requests(AdminStaffRequiredMixin,ListView):
    model=models.studentCourses
    template_name='eapp/request.html'
    context_object_name='list'
    def get_queryset(self):
        qs=super(Requests,self).get_queryset()
        #print(qs.filter(status__exact='False'))
        return qs.filter(status__exact='False')
class Detail(AdminStaffRequiredMixin,UpdateView):
    model=models.studentCourses
    template_name='eapp/details.html'
    fields=('status',)
    success_url=reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        req=models.studentCourses.objects.get(id=self.kwargs['pk'])

        context["usname"] = req
        context["pk"]=self.kwargs['pk']
        return context
class ReqDelete(AdminStaffRequiredMixin,DeleteView):
    model=models.studentCourses
    success_url='/'
