from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "age",
        "result",
        "created_at"
    )

    search_fields = (
        "name",
        "email"
    )

    list_filter = (
        "result",
        "sex"
    )