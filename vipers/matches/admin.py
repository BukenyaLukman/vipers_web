from django.contrib import admin

# Register your models here.

from .models import Match, Competition, MatchResult
admin.site.register(Match)
admin.site.register(Competition)
admin.site.register(MatchResult)
