from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Product
from .serializers import ProductSerializer

# GET by id view
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
     

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

product_detail_view = ProductDetailAPIView.as_view()

# UPDATE product view
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description= instance.name

product_update_view = ProductUpdateAPIView.as_view()

# DELETE product view
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def perfom_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()

# POST new product view
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     # serializer.save(user=self.request.user)
    #     name = serializer.validated_data.get('name')
    #     description = serializer.validated_data.get('description') or None
    #     if description is None:
    #         description = name

    #     print(serializer.validated_data)
    #     serializer.save()

    # same thing /\   \/   --> super().perfom_create(serializer) == serializer.save()

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        description = serializer.validated_data.get("description")
        if(description is None):
            description = name
            serializer.save(description=description)
        return super().perform_create(serializer)

product_create_view = ProductCreateAPIView.as_view()

# GET list view
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

product_list_view = ProductListAPIView.as_view()

# POST new product and GET product list!!
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'pk'

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = name

        print(serializer.validated_data)
        serializer.save(description=description)

product_list_create_view = ProductListCreateAPIView.as_view()

# ---------------------------------------------------------------------

# MIXIN VIEWS
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    #HTTP GET
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.list(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

# ---------------------------------------------------------------------

# ITS CONFUSING TU USE FUNCTION METHODS AS MULTIPLE ENDPOINTS
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":

        if pk is not None:
            # detail view

            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
    
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            description = serializer.validated_data.get('description') or None
            if description is None:
                description = name
            print(serializer.validated_data)
            serializer.save(description=description)

            return Response(serializer.data)
    
        return Response({"message": "invalid data."}, status=400)