from django.contrib import admin
from .models import Submission, User


# Register your models here.


class DefAdm(admin.ModelAdmin):
    pass


class CreateSubmission(admin.ModelAdmin):
    model = Submission
    fieldsets = (
        (None, {
            'fields': ('post_title', 'username', 'pub_date'),
        }),
    )

#
# class CreateUser(admin.ModelAdmin):
#     model = User


admin.site.register(User, DefAdm)
admin.site.register(Submission, CreateSubmission)
