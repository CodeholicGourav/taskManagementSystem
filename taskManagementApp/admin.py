from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(TaskTag)
admin.site.register(ColumnAttribute)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(CustomColumnValue)
admin.site.register(Permission)
admin.site.register(TaskAttribute)

# Added comment just to test github
