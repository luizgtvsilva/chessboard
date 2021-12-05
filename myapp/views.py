from django.db.models import query
from django.http import request
from rest_framework import generics, serializers
from .models import ChessB
from .serializers import ChessBSerializer, ChessKnightSerializer
from rest_framework.response import Response

class ChessBList(generics.ListCreateAPIView):
    queryset = ChessB.objects.all()
    serializer_class = ChessBSerializer

    def get_queryset(self):

        queryset = ChessB.objects.all()
        piece_name = self.request.query_params.get('piece_name')
        if piece_name is not None and piece_name == 'knight':
            queryset = ChessB.objects.filter(piece_name=piece_name)
            print('###IMPLEMENTAR MÉTODO DO KNIGHT EM UTILS.PY###')
        elif piece_name is not None:
            queryset = ChessB.objects.filter(piece_name=piece_name)
        return queryset
    
    
