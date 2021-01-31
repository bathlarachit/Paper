from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username
status_choice=(
('True','True'),
('False','False'),
)
class Courses(models.Model):
    title=models.CharField(max_length=256)
    faculty=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class studentCourses(models.Model):
    user=models.ForeignKey(auth.models.User,on_delete=models.CASCADE)
    courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
    status=models.CharField(choices=status_choice,default='False',max_length=20)
    def __str__(self):
        return self.user.username
class Exam(models.Model):
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    total_marks=models.PositiveIntegerField()
    start_time=models.DateTimeField(blank=True,null=True)
    end_time=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
status_choice=(
('True','True'),
('False','False'),
)
class TF(models.Model):
    question=models.TextField()
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    ans=models.CharField(choices=status_choice,max_length=20)
    marks=models.PositiveIntegerField()
    def __str__(self):
        return self.question
class discriptive(models.Model):
    question=models.TextField()
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    #ans=models.TextField(null=True,blank=True)
    #file=models.FileField(upload_to='uploads/% Y/% m/% d/')
    marks=models.PositiveIntegerField()
    def __str__(self):
        return self.question
class fillnblanks(models.Model):
    question=models.TextField()
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    def __str__(self):
        return self.question
# class dis_ans(models.Model):
#     student=
