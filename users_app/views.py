from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response


class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        # Override get_serializer method to set uid and token in the data.
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
        print(kwargs)
        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        # Override activation method to return a custom response.
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@schema(None)
def password_reset_view(request, uid, token):
    # Custom password reset view.
    return Response(
        {
            "uid": uid,
            "token": token
        }
    )
