from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from ffWarUserApi.models import User


class Authentication:
    def authenticate(self, mobile,password):
        try:
            result = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            raise serializers.ValidationError({"non_field_errors": ["MOBILE_NOT_FOUND"]})
        user = authenticate(username=mobile, password=password)
        if user is not None:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            # groups = ""
            # for g in user.groups.all():
            #     groups = groups + g.name + ","
            # if groups.endswith(','):
            #     groups = groups[:-1]
            #payload['auth'] = groups
            token = jwt_encode_handler(payload)
            return user, token
        else:
            raise serializers.ValidationError({"non_field_errors": ["INCORRECT_PIN"]})




