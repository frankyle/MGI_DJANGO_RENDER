from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  
    path('api/tradedetails/', include('tradedetails.urls')),  
    path('api/tradereasons/', include('tradereasons.urls')),  
    path('api/candleimages/', include('candleimages.urls')),  
    path('api/tradingindicators/', include('tradingindicators.urls')),  
    path('api/task/', include('task.urls')),  
    path('api/puzzles/', include('puzzles.urls')),  
    path('api/toys/', include('toys.urls')),  
    path('api/games/', include('games.urls')),  
    path('api/risktrades/', include('risktrades.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

































































# # TEMPORARY SUPERUSER CREATION FOR DEPLOYMENT ON RENDER
# from django.contrib.auth import get_user_model
# from django.db.utils import OperationalError

# User = get_user_model()

# try:
#     if not User.objects.filter(is_superuser=True).exists():
#         print("✅ Creating temporary superuser...")
#         User.objects.create_superuser(
#             email='magaifrank@gmail.com',
#             password='Magai!@#123',
#             first_name='Frank',
#             last_name='Magai'
#         )
#     else:
#         print("✅ Superuser already exists.")
# except OperationalError:
#     print("❌ Database not ready — skipping superuser creation.")
