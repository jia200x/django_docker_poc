from django.contrib import admin
from api.models import Reader, Tag, Transaction

# Register your models here.
admin.site.register(Reader)
admin.site.register(Tag)
admin.site.register(Transaction)
