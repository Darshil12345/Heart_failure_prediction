from django import forms

SEX_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

CHEST_PAIN_CHOICES = [
    ('ATA', 'ATA'),
    ('NAP', 'NAP'),
    ('ASY', 'ASY'),
    ('TA', 'TA')
]

RESTING_ECG_CHOICES = [
    ('Normal', 'Normal'),
    ('LVH', 'LVH'),
    ('ST', 'ST')
]

ANGINA_CHOICES = [
    ('Y', 'Yes'),
    ('N', 'No')
]

ST_SLOPE_CHOICES = [
    ('Up', 'Up'),
    ('Flat', 'Flat'),
    ('Down', 'Down')
]


class PredictionForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Full Name"
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Email Address"
            }
        )
    )

    age = forms.IntegerField(
        help_text="Healthy Range: 18 - 100 years",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )

    chest_pain_type = forms.ChoiceField(
        choices=CHEST_PAIN_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )

    resting_bp = forms.IntegerField(
        help_text="Normal Range: 90 - 120 mmHg",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    cholesterol = forms.IntegerField(
        help_text="Healthy: Below 200 mg/dL",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    fasting_bs = forms.IntegerField(
        help_text="0 = Normal, 1 = High",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    resting_ecg = forms.ChoiceField(
        choices=RESTING_ECG_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )

    max_hr = forms.IntegerField(
        help_text="Typical Range: 60 - 100 bpm",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    exercise_angina = forms.ChoiceField(
        choices=ANGINA_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )

    oldpeak = forms.FloatField(
        help_text="ST Depression (usually 0 - 6)",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.1"
            }
        )
    )

    st_slope = forms.ChoiceField(
        choices=ST_SLOPE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select"
            }
        )
    )