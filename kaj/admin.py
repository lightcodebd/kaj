from django.contrib import admin

# Register your models here.


from .models import JOB
from .models import JOBLOCATION
from .models import Education_Qualification 


admin.site.register(JOB)
admin.site.register(JOBLOCATION)
admin.site.register(Education_Qualification)
