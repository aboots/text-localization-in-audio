from django.urls import path, include

from . import views


urlpatterns = [

    path("", views.search),
    path("search_submit", views.search_submit),
    path("process/<int:id>", views.process),
    path("results/<int:id>", views.results),

    path("ping", views.ping),
    path("ping_template", views.ping_template),
]
