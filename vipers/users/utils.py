from django.conf import settings
import jwt


class Util:
    @staticmethod
    def decode_token(request):
        authorization = request.headers.get('Authorization')
        token = authorization.split(' ')[1]
        try:
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decode_token['user_id']
        except Exception as exceptions:
            return exceptions
        return user_id