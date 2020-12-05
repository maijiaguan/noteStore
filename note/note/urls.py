"""note URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from noteapp.views import NotesModelViewSet
from noteapp.views import (
    NotesPostView,
    NotesGetPatchDeleteView,
    NotesFolderPatchDeleteView,
    NotesFolderGetPostView,
    InitNotesListGetView,
    SearchNotesView,
    CategoryNotesView
)
# from category.views import CategoryModelViewSet
from category.views import (
    CategoryGetPostView,
    CategoryPatchDeleteView
)
from users.views import (
    UserProfileModelViewSet,
    SendCodeView,
    MyTokenObtainPairView
)
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# router.register(r'notes', NotesModelViewSet)
# router.register(r'category', CategoryModelViewSet)
router.register(r'userinfo', UserProfileModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path('login/', LoginView.as_view(), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', obtain_jwt_token),
    path('api/sendcode/', SendCodeView.as_view(), name='sendcode'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/category/', CategoryGetPostView.as_view(), name='category_get_post'),
    re_path(r'^api/category/(?P<pk>\d+)$',
            CategoryPatchDeleteView.as_view(), name='category_patch_delete'),

    path('api/notes/', NotesPostView.as_view(), name='notes_post'),
    re_path(r'^api/notes/([0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12})/$',
            NotesGetPatchDeleteView.as_view(), name='notes_get_patch_delete'),

    path('api/folder/', NotesFolderGetPostView.as_view(), name='folder_get_post'),
    re_path(r'^api/folder/([0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12})/$',
            NotesFolderPatchDeleteView.as_view(), name='folder_patch_delete'),

    path('api/notelists/', InitNotesListGetView.as_view(), name='notelists_get'),

    path('api/searchnote/', SearchNotesView.as_view(), name='searchnote'),

    re_path(r'^api/categorynotes/(?P<ci>\d+)$',
            CategoryNotesView.as_view(), name='category_notes'),
]
