from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response


class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
        print(kwargs)
        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@schema(None)
def password_reset_view(request, uid, token):
    return Response(
        {
            "uid": uid,
            "token": token
        })
