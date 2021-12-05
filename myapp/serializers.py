from rest_framework import serializers
from .models import ChessB

class ChessBSerializer(serializers.ModelSerializer):

    class Meta:

        model = ChessB
        fields = ('id',)

class ChessKnightSerializer(serializers.ModelSerializer):

    class Meta:

        model = ChessB
        fields = ('id','possible_movement')