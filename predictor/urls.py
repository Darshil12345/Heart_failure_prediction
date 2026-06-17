from django.urls import path

from .views import (
    home,
    predict,
    history,
    delete_prediction,
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'predict/',
        predict,
        name='predict'
    ),
    path(
        'history/',
        history,
        name='history'
    ),
    path(
        'delete/<int:id>/',
        delete_prediction,
        name='delete_prediction'
    ),
    
]