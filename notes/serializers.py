from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'text', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'notes']

class UserCreateSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'notes']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        notes_data = validated_data.pop('notes')
        user = User.objects.create_user(**validated_data)
        for note_data in notes_data:
            Note.objects.create(author=user, **note_data)
        return user
