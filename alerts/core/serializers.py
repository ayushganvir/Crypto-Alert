# from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import CoinAlert

from name_script import get_coin_names


class UserSerializer(serializers.ModelSerializer):
    # alerts = serializers.PrimaryKeyRelatedField(many=True, read_only= True)
    alerts = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['url', 'username', 'alerts']


class CoinAlertSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='created_by.username')
    status = serializers.ReadOnlyField()

    class Meta:
        model = CoinAlert
        fields = ['id', 'coin_symbol', 'buy_price', 'alert_price', 'status', 'user']

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
