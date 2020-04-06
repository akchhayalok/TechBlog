from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','status','created_on')
	list_filter = ("status",)
	search_fields=['title','content']
	prepopolated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


