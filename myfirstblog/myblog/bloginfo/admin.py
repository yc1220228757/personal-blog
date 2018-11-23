from django.contrib import admin
from .models import * 

admin.site.register(Categorya)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Save)

