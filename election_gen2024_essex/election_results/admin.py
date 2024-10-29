from django.contrib import admin
from .models import GEResults


# Register your models here.
class GEResultsAdmin(admin.ModelAdmin):
    list_display = (
        "constituency",
        "conservative",
        "labour",
        "liberaldemocrat",
        "reform",
    )


admin.site.register(GEResults, GEResultsAdmin)
