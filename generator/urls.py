from django.urls import path
from .views import display_all_images_view, generate_image_view, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Home page with text inputs
    path('generate/', generate_image_view, name='generate_image'),  # Generate page
    path('all/', display_all_images_view, name='display_all_images'),  # Show all images page
]
