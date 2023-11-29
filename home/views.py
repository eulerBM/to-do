from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import to_do_bank
from home.serializers import Serializer_bank

@api_view(['GET'])
def list_todos(request):
    if request.method == 'GET':
        try:
            all_itens = to_do_bank.objects.all()
            serializer = Serializer_bank(all_itens, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({"message": "Essa url so aceita GET (Pegar)!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def list_pegar(request, pk):
    if request.method == 'GET':
        try:
            item = to_do_bank.objects.get(key=pk)
            serializer = Serializer_bank(item, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "Essa url so aceita GET (Pegar)!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def list_criar(request):
    if request.method == 'POST':
        try:
            serializer = Serializer_bank(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "Essa url so aceita POST (Criar)!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def list_atualizar(request, pk):
    if request.method == "PUT":
        try:
            item = to_do_bank.objects.get(key=pk)
            serializer = Serializer_bank(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "Essa url so aceita PUT (Atualizar)!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def list_deletar(request, pk):
    if request.method == "DELETE":
        try:
            item = to_do_bank.objects.get(key=pk)
            item.delete()
            return Response({"message": "Objeto excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message": "Essa url so aceita DELETE (Delete)!"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)










    





