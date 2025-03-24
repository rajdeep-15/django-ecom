from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer,ProductSerializer,CartItemSerializer
from ecommerce.models import Product,CartItem
# Create your views here.


class RegisterView(APIView):

    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)

        if user:
            token = RefreshToken.for_user(user=user)
            return Response({'access': str(token.access_token),
                             'refresh':str(token)},
                             status=status.HTTP_200_OK)
        return Response({"error:INVALID CREDENTIALS"},status = status.HTTP_400_BAD_REQUEST)
    


#TODO : try with simple API if it doesn't work
class ProductListCreateView(ListCreateAPIView):

    '''add a product and list them all'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CartItemListCreateView(ListCreateAPIView):
    '''Cartitem table has the user details and the product details'''

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        product_id = self.request.data.get('product')  # Get product ID from request
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = Product.objects.get(id=product_id)  # Validate product exists
        except Product.DoesNotExist:
            return Response({"error": "Invalid product ID"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=self.request.user, product=product)
        serializer.save(user = self.request.user)


class CartItemDetailview(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user)