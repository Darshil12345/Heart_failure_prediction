from django.contrib.auth.models import User
from django.db import models

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)


class Prediction(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(100)
        ]
    )

    sex = models.CharField(
        max_length=1
    )

    chest_pain_type = models.CharField(
        max_length=10
    )

    resting_bp = models.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(250)
        ]
    )

    cholesterol = models.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(700)
        ]
    )

    fasting_bs = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )

    resting_ecg = models.CharField(
        max_length=10
    )

    max_hr = models.IntegerField(
        validators=[
            MinValueValidator(60),
            MaxValueValidator(220)
        ]
    )

    exercise_angina = models.CharField(
        max_length=1
    )

    oldpeak = models.FloatField(
        validators=[
            MinValueValidator(0)
        ]
    )

    st_slope = models.CharField(
        max_length=10
    )

    result = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.name} - "
            f"{self.age} - "
            f"{self.result}"
        )