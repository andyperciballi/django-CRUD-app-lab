from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wallpapers/', views.WallpaperList.as_view(), name='wallpaper-index'),
    path('wallpapers/create/', views.WallpaperCreate.as_view(), name='wallpaper-create'),
    path('wallpapers/<int:pk>/', views.wallpaper_detail, name='wallpaper-detail'),
    path('wallpapers/<int:wallpaper_id>/add-use-log/', views.add_use_log, name='add-use-log'),
    path('wallpapers/<int:wallpaper_id>/associate-tag/<int:tag_id>/', views.associate_tag, name='associate-tag'),
    path('wallpapers/<int:pk>/update/', views.WallpaperUpdate.as_view(), name='wallpaper-update'),
    path('wallpapers/<int:pk>/delete/', views.WallpaperDelete.as_view(), name='wallpaper-delete'),
    path('tags/', views.TagList.as_view(), name='tag-list'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
]