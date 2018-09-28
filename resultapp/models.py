from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
	"""docstring for Student"""
	admin_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	surname = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	othernames = models.CharField(max_length=200)
	sex = models.CharField(max_length=50)
	dob = models.DateTimeField()
	age = models.IntegerField()
	parent_name = models.CharField(max_length=200)
	address = models.CharField(max_length=250)
	#student_class = models.ForeignKey('student_class', on_delete=models.CASCADE)
	#student_class_arm = models.ForeignKey('Class_arms',on_delete=models.CASCADE)
	email = models.EmailField(max_length=200)
	phone_number = models.CharField(max_length=20)
	registration_date = models.DateTimeField(default=timezone.now)


	def register(self):
		self.registration_date = timezone.now()
		self.save()

	def __str__(self):
		return self.surname + self.firstname