from django.contrib import admin
from accounts.models import mobile,Doctor,Schedule,Appointment

class mob(admin.ModelAdmin):
    list_display= ('phone', 'u')

admin.site.register(mobile,mob)   

class doc(admin.ModelAdmin):
    list_display= ('did', 'dname','dmobile','qualification','specialist','yoe') 
    
admin.site.register(Doctor,doc)

class sch(admin.ModelAdmin):
    list_display= ('sid', 'time_slot','doctor') 
    
admin.site.register(Schedule,sch)    

class app(admin.ModelAdmin):
    list_display= ('apid', 'user','doctor','appdate') 
    
admin.site.register(Appointment,app)        