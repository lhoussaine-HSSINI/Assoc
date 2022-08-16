from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import AssociationAdminSignupSerializer, AssociationSerializer,UserSerializer,GuestSerializer, AssociationMemberSignupSerializer, OrganizationAdminSignupSerializer,MemberSerializer,OrganizationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User, Association , Memberassociation , Organization
from rest_framework import  generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from  rest_framework.permissions import IsAuthenticated, AllowAny



# start Association
class add_association(viewsets.ModelViewSet):
    queryset = Association.objects.all()
    permission_classes = [AllowAny]
    serializer_class = AssociationSerializer

class add_membre(viewsets.ModelViewSet):
    queryset = Memberassociation.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MemberSerializer

class add_organization(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permission_classes = [AllowAny]
    serializer_class = OrganizationSerializer

class AssociationList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, form=None):
        associations = Association.objects.all()
        serializer = AssociationSerializer(associations, many=True)
        return  Response(data=serializer.data)

# end Association

class GtList(generics.ListCreateAPIView):
    queryset = Association.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer



class GDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Association.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer

class AssociationAdminSignup(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class=AssociationAdminSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account admin created successfully"
        })

class AssociationMemberSignup(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class=AssociationMemberSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account member created successfully"
        })
class OrganizationAdminSignup(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class=OrganizationAdminSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "token":Token.objects.get(user=user).key,
            "message":"account admin created successfully"
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid() :
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created=Token.objects.get_or_create(user=user)
            return Response({
                'is_authenticated':user.is_authenticated,
                'token':token.key,
                'user_id':user.pk,
                'is_admin_assoc':user.is_admin_assoc,
                'is_member_assoc': user.is_member_assoc,
                'is_admin_orga': user.is_admin_orga,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
        else:
            return Response({'message':'Invalid username or email ', 'is_authenticated':False})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        return Response(data=content, status=status.HTTP_200_OK)


