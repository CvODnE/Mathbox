from django.contrib import admin
from web.models import Faq, CommmunityPost, Exercises, Games, Tools, Kids, KidsPlay, Student, StudentPlay


class FaqAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]

admin.site.register(Faq, FaqAdmin)


class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ["heading", "image", "content"]

admin.site.register(CommmunityPost, CommunityPostAdmin)

class ExercisesAdmin(admin.ModelAdmin):
    list_display = ["about", "html", "css", "js", "type"]

admin.site.register(Exercises, ExercisesAdmin)

class GamesAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "html", "css", "js", "type"]

admin.site.register(Games, GamesAdmin)


class ToolsAdmin(admin.ModelAdmin):
    list_display = ["name", "html", "css", "js"]

admin.site.register(Tools, ToolsAdmin)


class KidsPlayInline(admin.TabularInline):
    model = KidsPlay
    extra = 1
    can_delete = True
    fields = ('value','link')

# Main model admin
class KidsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "item", "play_count")
    inlines = [KidsPlayInline]
    

    def play_count(self, obj):
        return obj.plays.count()
    play_count.short_description = 'Play Count'


admin.site.register(Kids, KidsAdmin)
admin.site.register(KidsPlay)


class StudentPlayInline(admin.TabularInline):
    model = StudentPlay
    extra = 1
    can_delete = True
    fields = ('value','link')

# Main model admin
class StudentAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "item", "play_count")
    inlines = [StudentPlayInline]
    

    def play_count(self, obj):
        return obj.plays.count()
    play_count.short_description = 'Play Count'


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentPlay)