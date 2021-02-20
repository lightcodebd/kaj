from django.db import models
from django.contrib.auth.models import User


# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Pending")
)

TYPES = (
        (0, "BD Govt Job"),
        (1, "Private Job"),
        (2, "Question"),
        (3, "Cercular")
)


class Education_Qualification(models.Model):
    examname = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.examname

class JOBLOCATION(models.Model):
    location = models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return self.location

class JOB(models.Model):
    jobtitle = models.CharField(max_length=200, unique=True)
    jobdescription = models.TextField()
    jobpublished = models.DateTimeField()
    apply_start = models.DateTimeField()
    apply_last_date = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    jobdescription = models.TextField()
    joblocation = models.ForeignKey(JOBLOCATION, on_delete= models.CASCADE,related_name='joblocation')
    education_qualification=models.ForeignKey(Education_Qualification, on_delete= models.CASCADE,related_name='joblocation')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    types = models.IntegerField(choices=TYPES, default=4) 
    source_link = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='kajpost')
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



