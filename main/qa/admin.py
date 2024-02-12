from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')  # Display these fields in the list view
    search_fields = ('title', 'detail')  # Enable searching by these fields

# Register the Question model with the custom admin class
admin.site.register(Question, QuestionAdmin)

# Register the Answer model without any custom admin class
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(UpVote)
admin.site.register(DownVote)