from . import views
import django.urls as urls
urlpatterns = [
    urls.path("home/", views.home, name="home"),
    urls.path("about/page/page1/<int:id>/", views.about, name="about"),
    urls.path("contact/", views.contact, name="contact"),
]