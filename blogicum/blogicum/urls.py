from django.urls import path, include

urlpatterns = [
    path("", include("blog.urls")),
    path("posts/", include("blog.urls")),
    path("category/", include("blog.urls")),
    path("pages/", include("pages.urls")),
]
