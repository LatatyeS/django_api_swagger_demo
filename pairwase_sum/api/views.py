from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


SAMPLE_RESP ={
    "200": openapi.Response(
        description="Сложение проведено",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT, 
            properties={
                'output': openapi.Schema(type=openapi.TYPE_STRING, description='3,7'),
        }),
        examples={
            "application/json": {
                        "output": "3,7"
            }
        }
    ),
    "400": openapi.Response(
        description="Неверный формат входных данных",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT, 
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Неверный формат входных данных. Встречаются не числа'),
        }),
        examples={
            "application/json": {
                        "message": "Неверный формат входных данных. Встречаются не числа"
            }
        }
    ),
}

def make_math(row):
    output = [0] * (len(row) // 2)
    for i, element in enumerate(row):
        output[i // 2] += element
    return ','.join(map(lambda x: str(x), output))


@swagger_auto_schema(
    methods=['post'], 
    operation_id='api/v1/calculate',
    operation_description='Производит попарное суммирование входящих данных',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'input': openapi.Schema(type=openapi.TYPE_STRING, description='1,2,3,4'),
    }),
    responses = SAMPLE_RESP
)
@api_view(['POST'])
def calculate(request):

    data = request.data

    if not 'input' in data.keys():
        return Response(
                {'message': 'Неверный формат входных данных. Нет поля "input"'}, 
                status=status.HTTP_400_BAD_REQUEST
        )
    
    if not isinstance(data['input'], str):
        return Response(
                {'message': 'Неверный формат входных данных. "input" - не является списком'}, 
                status=status.HTTP_400_BAD_REQUEST
        )

    if not all([item.replace('.','',1).isdigit() for item in data['input'].split(',')]):
        return Response(
                {'message': 'Неверный формат входных данных. Встречаются не числа'}, 
                status=status.HTTP_400_BAD_REQUEST
        )

    if len(data['input'].split(',')) % 2 != 0:
        return Response(
                {'message': 'Неверный формат входных данных. Нечетное число в ряде чисел'}, 
                status=status.HTTP_400_BAD_REQUEST
        )

    try:
        output = make_math(list(map(lambda x: int(x), data['input'].split(','))))
        return Response(
            {'message': 'Сложение проведено', 'output': output},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'message': 'Неверный формат данных'},
            status=status.HTTP_400_BAD_REQUEST
        )

