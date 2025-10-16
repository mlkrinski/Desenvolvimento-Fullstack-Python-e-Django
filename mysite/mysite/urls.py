from mysite.admin import admin_site
from django.urls import path, include


urlpatterns = [
    path("admin/", admin_site.urls),
    path("polls/", include("polls.urls")),
    path("contacts/", include("contacts.urls")),
    path("accounts/", include("accounts.urls")),
]
