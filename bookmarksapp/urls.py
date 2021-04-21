from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/delete/', views.Deletebookmarks, name='delete-bookmarks'),
    path('<int:pk>/bookmarkdetail/', views.Detailbookmarks, name='detail-bookmarks'),
    path('<int:pk>/bookmarkupdate/', views.Updatebookmarks, name='update-bookmarks'),
    path('<int:pk>/folder/', views.FolderList, name='list-folder'),
]