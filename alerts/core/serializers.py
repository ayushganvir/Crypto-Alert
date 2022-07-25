# from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import CoinAlert

from name_script import get_coin_names


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'])


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # alerts = serializers.PrimaryKeyRelatedField(many=True, read_only= True)
    # alerts = serializers.ReadOnlyField()
    # url = serializers.HyperlinkedIdentityField(view_name='user-detail', read_only=True)
    alerts = serializers.HyperlinkedRelatedField(many=True, view_name='alert-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'alerts']


class UserAlertSerializer(serializers.Serializer):
    # created_by = serializers.CharField(required=True)
    # password = serializers.CharField(required=True)
    coin_symbol = serializers.CharField()
    buy_price = serializers.IntegerField()
    alert_price = serializers.IntegerField()

    def create(self, validated_data):
        print(validated_data)
        return CoinAlert.objects.create(created_by=User.objects.get(username = validated_data['created_by']),
                                        coin_symbol=validated_data['coin_symbol'],
                                        buy_price=validated_data['buy_price'],
                                        alert_price=validated_data['alert_price']
                                        )


class CoinAlertSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='created_by.username')
    status = serializers.ReadOnlyField()

    class Meta:
        model = CoinAlert
        fields = ['id', 'coin_symbol', 'buy_price', 'alert_price', 'status', 'user']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'])
        return user

#     def get_user(self, obj):
#         return {'id': obj.created_by.id, 'name': obj.created_by.username}
# #
# class CoinAlertSerializer(serializers.Serializer):
#     coin_names = get_coin_names()
#     STATUS_CHOICES = (('C', 'Created'), ('D', 'Deleted'), ('T', 'Triggered'))
#
#     id = serializers.IntegerField(read_only=True)
#     coin_symbol = serializers.ChoiceField(choices=coin_names, default='Bitcoin')
#     buy_price = serializers.IntegerField()
#     alert_price = serializers.IntegerField()
#     status = serializers.ChoiceField(choices=STATUS_CHOICES)
#
#     def create(self, validated_data):
#         return CoinAlert.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.coin_symbol = validated_data.get('coin_symbol', instance.coin_symbol)
#         instance.buy_price = validated_data.get('buy_price', instance.buy_price)
#         instance.alert_price = validated_data.get('alert_price', instance.alert_price)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance
#
