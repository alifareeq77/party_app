import logging
from django.db import close_old_connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from channels.db import database_sync_to_async


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        await database_sync_to_async(close_old_connections)()

        # Get the token
        token = parse_qs(scope["query_string"].decode("utf8")).get("token", [None])[0]

        # Try to authenticate the user
        try:
            if not token:
                raise InvalidToken("Token is missing")

            UntypedToken(token)
        except (InvalidToken, TokenError) as e:
            logging.error(f"Token validation failed: {e}")
            return None
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            logging.debug(f"Decoded token data: {decoded_data}")

            try:
                # Get the user using ID
                user = await database_sync_to_async(get_user_model().objects.get)(id=decoded_data["user_id"])
            except get_user_model().DoesNotExist:
                logging.error(f"User not found with ID: {decoded_data['user_id']}")
                return None

        return await self.inner(dict(scope, user=user), receive, send)
