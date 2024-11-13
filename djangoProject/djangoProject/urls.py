from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoHome.urls')),
    path('profile/', include('djangoProfile.urls')),
    path('blog/', include('djangoPosts.urls')),
]
