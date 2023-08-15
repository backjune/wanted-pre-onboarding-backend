from rest_framework import generics
from rest_framework.response import Response

from user.models import User
from .models import Board
from .serializers import BoardSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class BoardListPagination(PageNumberPagination):
    page_size = 5


class BoardList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    pagination_class = BoardListPagination


class BoardCreate(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': '해당하는 유저가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        Board.objects.create(owner=user, content=request.data.get('content'))
        return Response(status=status.HTTP_201_CREATED)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = int(request.data.get('user_id'))
        board_owner_id = instance.owner.id

        if user_id == board_owner_id:
            return super().update(request, *args, **kwargs)

        return Response(
            {"error": "작성자만 수정 할 수 있습니다."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = int(request.data.get('user_id'))
        board_owner_id = instance.owner.id

        if user_id == board_owner_id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {"error": "작성자만 삭제 할 수 있습니다."},
            status=status.HTTP_401_UNAUTHORIZED
        )
