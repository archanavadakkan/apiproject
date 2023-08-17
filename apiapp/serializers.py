from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()


class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    mobile = serializers.CharField()

    class Meta:
        model = User
        fields = ["username","password","email","password2","mobile"]

    def save(self):
        reg = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        mobile = self.validated_data['mobile']

        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg
