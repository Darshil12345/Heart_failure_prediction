from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import PredictionForm
from .models import Prediction

from .services.predictor import (
    predict_heart_disease
)


def home(request):

    return render(
        request,
        "home.html"
    )


@login_required
def predict(request):

    result = None

    confidence = None

    if request.method == "POST":

        form = PredictionForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]

            email = form.cleaned_data["email"]

            age = form.cleaned_data["age"]

            sex = form.cleaned_data["sex"]

            chest_pain_type = form.cleaned_data[
                "chest_pain_type"
            ]

            resting_bp = form.cleaned_data[
                "resting_bp"
            ]

            cholesterol = form.cleaned_data[
                "cholesterol"
            ]

            fasting_bs = form.cleaned_data[
                "fasting_bs"
            ]

            resting_ecg = form.cleaned_data[
                "resting_ecg"
            ]

            max_hr = form.cleaned_data[
                "max_hr"
            ]

            exercise_angina = form.cleaned_data[
                "exercise_angina"
            ]

            oldpeak = form.cleaned_data[
                "oldpeak"
            ]

            st_slope = form.cleaned_data[
                "st_slope"
            ]

            prediction_data = predict_heart_disease(

                age,

                sex,

                chest_pain_type,

                resting_bp,

                cholesterol,

                fasting_bs,

                resting_ecg,

                max_hr,

                exercise_angina,

                oldpeak,

                st_slope

            )

            prediction = prediction_data[
                "prediction"
            ]

            confidence = prediction_data[
                "confidence"
            ]

            if prediction == 1:

                result = "Heart Disease"

            else:

                result = "No Heart Disease"

            Prediction.objects.create(

                user=request.user,

                name=name,

                email=email,

                age=age,

                sex=sex,

                chest_pain_type=chest_pain_type,

                resting_bp=resting_bp,

                cholesterol=cholesterol,

                fasting_bs=fasting_bs,

                resting_ecg=resting_ecg,

                max_hr=max_hr,

                exercise_angina=exercise_angina,

                oldpeak=oldpeak,

                st_slope=st_slope,

                result=result

            )

    else:

        form = PredictionForm()

    return render(

        request,

        "predict.html",

        {

            "form": form,

            "result": result,

            "confidence": confidence

        }

    )


@login_required
def history(request):

    query = request.GET.get(
        "q"
    )

    predictions = Prediction.objects.filter(
        user=request.user
    )

    if query:

        predictions = predictions.filter(

            Q(name__icontains=query)

            |

            Q(email__icontains=query)

        )

    predictions = predictions.order_by(
        "-created_at"
    )

    paginator = Paginator(

        predictions,

        10

    )

    page_number = request.GET.get(
        "page"
    )

    page_obj = paginator.get_page(
        page_number
    )

    return render(

        request,

        "history.html",

        {

            "page_obj": page_obj,

            "query": query

        }

    )


@login_required
def delete_prediction(request, id):

    prediction = Prediction.objects.get(

        id=id,

        user=request.user

    )

    prediction.delete()

    return redirect(
        "history"
    )