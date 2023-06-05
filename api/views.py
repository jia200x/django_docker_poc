from django.shortcuts import render
from api.models import Reader
from api.models import Tag
from api.models import Transaction
from api.serializers import ReaderSerializer
from api.serializers import TagSerializer
from api.serializers import TransactionSerializer
from datetime import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes

from django.db.models import Count, Q

import json
import base64
import cbor2

# Create your views here.

class ReaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def transaction(self, request, pk=None):
        _from = request.query_params.get("from", None)
        _to = request.query_params.get("to", None)

        if _from is not None and _to is not None:
            _from = datetime.fromisoformat(_from.replace('Z', '+00:00'))
            _to = datetime.fromisoformat(_to.replace('Z', '+00:00'))

        objs = Reader.objects.annotate(num_beacons=Count('transaction__tag', filter=Q(transaction__timestamp__gte=_from) & Q(transaction__timestamp__lte=_to)))
        print(objs)

        # TODO: Add serializer...

        a = []
        for o in objs:
            a.append({"reader": ReaderSerializer(o).data, "num_beacons": o.num_beacons, "from": _from, "to": _to})
        
        return Response(a)


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_transaction(request):
    raw_payload = request.data["payload_raw"]
    base64_bytes = raw_payload.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)

    arr = cbor2.loads(message_bytes)
    deveui = request.data["hardware_serial"]
    r = Reader.objects.get(deveui=deveui)

    for a in arr:
        tag_id = int.from_bytes(a, "big")
        t = Tag.objects.get(pk=tag_id)

        Transaction.objects.create(reader=r, tag=t)
    return Response()
