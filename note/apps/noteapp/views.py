from django.db.models import Q
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notes, NotesFolder
from .serializers import (
    NotesModelSerializer,
    NotesFolderModelSerializer,
    InitNotesModelSerializer,
    SearchNotesModelSerializer
)
from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission

#
# class IsAuthenticated(BasePermission):
#     message = '查无此人'
#
#     def has_permission(self, request, view):
#         User_id = request.query_params.get("user_id")
#         user = Notes.objects.filter(user_id=int(User_id)).all()
#         if user:
#             return True
#         else:
#             print(self.message)
#             return False


# class NotesModelViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     permission_classes = []
#     queryset = Notes.objects.all()
#     serializer_class = NotesModelSerializer
#
#     # def get_queryset(self):
#     #     Note_title = self.request.query_params.get("note_title")
#     #     note = Notes.objects.filter(note_title=Note_title)
#     #     queryset = note
#     #     return queryset
#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user)


class InitNotesListGetView(APIView):
    """
    登录后的初始化，查找笔记列表
    """
    # 查
    def get(self, request, format=None):
        user_notelists = Notes.objects.filter(user=request.user)
        serializer = InitNotesModelSerializer(user_notelists, many=True)
        return Response(serializer.data)


class NotesPostView(APIView):
    """
    添加笔记
    """
    # 增
    def post(self, request, format=None):
        serializer = NotesModelSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesGetPatchDeleteView(APIView):
    """
    修改笔记和删除笔记
    """
    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404
    # 查
    def get(self, request, pk, format=None):
        # note = self.get_object(pk)
        user_notes = Notes.objects.filter(note_uid=pk, user=request.user)
        print(user_notes, 1, pk)
        serializer = NotesModelSerializer(user_notes, many=True)
        # return Response(serializer.data)
        if user_notes:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 改
    def patch(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NotesModelSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 删
    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        if note.user_id == request.user.user_uid:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class NotesFolderGetPostView(APIView):
    """
    查找笔记本和添加笔记本
    """
    # 查
    def get(self, request, format=None):
        user_folder = NotesFolder.objects.filter(user=request.user)
        serializer = NotesFolderModelSerializer(user_folder, many=True)
        return Response(serializer.data)
    # 增
    def post(self, request, format=None):
        serializer = NotesFolderModelSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesFolderPatchDeleteView(APIView):
    """
    修改笔记本和删除笔记本
    """
    def get_object(self, pk):
        try:
            return NotesFolder.objects.get(pk=pk)
        except NotesFolder.DoesNotExist:
            raise Http404
    # 改
    def patch(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = NotesFolderModelSerializer(folder, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 删
    def delete(self, request, pk, format=None):
        folder = self.get_object(pk)
        if folder.user_id == request.user.user_uid:
            folder.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SearchNotesView(APIView):
    """
    搜索笔记
    """
    def get(self, request):
        keyword = request._request.GET.get('keyword')
        # print(keyword)
        if keyword:
            note_title = Notes.objects.filter(
                Q(note_title__icontains=keyword) |
                Q(note_content_v1__icontains=keyword) |
                Q(note_content_v2__icontains=keyword) |
                Q(note_content_v3__icontains=keyword),
                user=request.user
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        re = SearchNotesModelSerializer(note_title, many=True)
        return Response(re.data)


class CategoryNotesView(APIView):
    # ci是category_id
    def get_object(self, ci):
        try:
            return Notes.objects.get(category_id=ci)
        except Notes.DoesNotExist:
            raise Http404
    # 查
    def get(self, request, ci, format=None):
        # note = self.get_object(pk)
        user_notes = Notes.objects.filter(category_id=ci, user=request.user)
        print(user_notes, 1, ci)
        serializer = InitNotesModelSerializer(user_notes, many=True)
        # return Response(serializer.data)
        if user_notes:
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)