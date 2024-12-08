try:
    # Define the updated content for urls.py to include static file handling for media
    urls_content = """
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""

    # Step 1: Write the updated content to urls.py, completely overwriting it
    with open("/home/scisoftdev/PycharmProjects/slai/Project/slai/urls.py", "w") as file:
        file.write(urls_content)

    print("Program executed successfully: urls.py has been updated to serve media files during development.")
except Exception as e:
    print("Program execution failed:", e)