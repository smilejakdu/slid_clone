from django.urls  import path
from folder.views import FolderView

urlpatterns = [
    path('', FolderView.as_view())
]
