from django.contrib import admin
from blog.models import Carousel,Article,Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','create_time','view_counter','tags')
    list_filter = ('create_time',)
    fields = ('author','title','content','summary','img','tags')


class CarouselAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','img','create_time')
    list_filter = ('create_time',)
    fields = ('title','img','summary','article')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','create_time','user')
    list_filter = ('create_time',)
    fields = ('article','text','user')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(Comment,CommentAdmin)

