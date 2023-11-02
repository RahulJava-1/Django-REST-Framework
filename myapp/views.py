from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializers
from rest_framework.views import APIView
from .models import Todo

# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])

def index(request):
    if request.method == "POST":
        return Response(
            {
                'status':200,
                'message':'DRF',
                'Method_called':"You Called POST method"

            }
        )
    elif request.method == "GET":
        return Response(
            {
                'status':'200',
                'message':'Smoothly run',
                'Method_called':'GET'
            }
        )
    elif request.method == 'PATCH':
        return Response({
            'status':'200',
            'message':'Fantastic PATCH',
            'method_called':'PATCH'
        })
    else:
        return Response({
            'status':'400',
            'message':'ERROR',
            'method_called':'Unknown Method'
        })

@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializers(todo_objs, many=True)

    return Response({
        'status':True,
        'message':'fetched',
        'data':serializer.data
    })



@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'message': 'Correct',
                'data': serializer.data
            })

        else:
            return Response({
            'status': False,
            'message':'Kindly fill the required fields',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)

    return Response({
        'status': False,
        'message':'something went wrong'
    })       


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data=request.data
        if not data.get('uid'):
            return Response({
                'status':False,
                'message': 'uid is required',
                'data':{}
            })
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializers(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status':True,
                'message': 'Correct',
                'data': serializer.data
            })
        else:
            return Response({
            'status': False,
            'message':'Invalid Data',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Invalid UID',
            'data':{}
        })
    

#Class Based API View
class TodoView(APIView):
    def get(self,request):
        todo_objs = Todo.objects.all()
        serializer = TodoSerializers(todo_objs, many=True)

        return Response({
            'status':True,
            'message':'fetched',
            'data':serializer.data
        })
    
    def post(self,request):
        try:
            data = request.data
            serializer = TodoSerializers(data=data)
        
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
                    'status':True,
                    'message': 'Correct',
                    'data': serializer.data
                })

            else:
                return Response({
                'status': False,
                'message':'Kindly fill the required fields',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)

        return Response({
            'status': False,
            'message':'something went wrong'
        })       

    def patch(self, request):
        try:
            data=request.data
            if not data.get('uid'):
                return Response({
                    'status':False,
                    'message': 'uid is required',
                    'data':{}
                })
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializers(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
                    'status':True,
                    'message': 'Correct',
                    'data': serializer.data
                })
            else:
                return Response({
                'status': False,
                'message':'Invalid Data',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status':False,
                'message':'Invalid UID',
                'data':{}
            })