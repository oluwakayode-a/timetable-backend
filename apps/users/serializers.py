from .models import User
from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        extra_kwargs = {"password" : {"write_only" : True}}
    
    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user
    
    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email has already been used.")
        return email