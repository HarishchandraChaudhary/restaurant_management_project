from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        )
        read_only_fields = ('id','username',)
    def update(self,instance,validated_data):

        if 'email' in validated_data:
            instance.email = validated_data.get('email',instance.email)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)

        instance.save()
        return instance
