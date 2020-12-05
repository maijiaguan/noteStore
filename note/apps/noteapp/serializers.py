from rest_framework import serializers
from rest_framework.fields import empty

from category.models import Category
from category.serializers import CategoryModelSerializer
from .models import Notes, NotesFolder


class NotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        read_only_fields = ('note_uid', 'user')


class NotesFolderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesFolder
        fields = "__all__"
        read_only_fields = ('folder_uid', 'user')


class InitNotesModelSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField(read_only=True)
    # def get_category_color(self, obj):
    #     return obj.get_category_color()
    #     category_query_set = obj.category.all()
    #     return [{"id": category_obj.id, "category_color": category_obj.category_color}
    #             for category_obj in category_query_set]
    # note_content_v1 = serializers.CharField(max_length=2)
    category = CategoryModelSerializer()

    class Meta:
        model = Notes
        # fields = "__all__"
        exclude = ("note_content_v2", "note_content_v3")
        read_only_fields = ('note_uid', 'user')
        # depth = 1


class SearchNotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('note_uid', 'note_title')
