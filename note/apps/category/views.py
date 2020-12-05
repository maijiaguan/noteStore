from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategoryModelSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission


# class IsAuthenticated(BasePermission):
#     message = '查无此用户'
#
#     def has_permission(self, request, view):
#         User_id = request.query_params.get("user_id")
#         user = Category.objects.filter(user_id=int(User_id)).all()
#         if user:
#             return True
#         else:
#             print(self.message)
#             return False


# class CategoryModelViewSet(viewsets.ModelViewSet):
#     # authentication_classes = []
#     # permission_classes = []
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer
#
#     # def get_queryset(self):
#     #     Category_id = self.request.query_params.get("category_id")
#     #     category = Category.objects.filter(id=int(Category_id))
#     #     queryset = category
#     #     return queryset
#     def perform_create(self, serializer):
#         serializer.save(user_uid=self.request.user)
class CategoryGetPostView(APIView):
    """
    获取标签和添加标签
    """
    # 查
    def get(self, request, format=None):
        user_category = Category.objects.filter(user=request.user)
        serializer = CategoryModelSerializer(user_category, many=True)
        return Response(serializer.data)
    # 增
    def post(self, request, format=None):
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryPatchDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    # 改
    def patch(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryModelSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # 删
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        # print(category.user, request.user, category.user_id, request.user.user_uid)
        if category.user_id == request.user.user_uid:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


