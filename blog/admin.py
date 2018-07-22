from django.contrib import admin
from blog.models import Carousel

# Register your models here.
class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','img','create_time')
    list_filter = ('create_time',)
    fields = ('title','img','summary')


admin.site.register(Carousel,CarouselAdmin)
