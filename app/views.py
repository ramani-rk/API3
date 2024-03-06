from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class ProductCrud(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JPO=ProductModelSerializers(LPO,many=True)
        return Response(JPO.data)
    
    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JPO=ProductModelSerializers(PO)
        return Response(JPO.data)
    
    def create(self,request):
        JO=request.data
        PO=ProductModelSerializers(data=JO)

        if PO.is_valid():
            PO.save()
            return Response ({'Create':'Data is Created Successfully'})
        else:
            return Response({'Error' : 'Data is Not Created'})
    
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JO=request.data
        PDO=ProductModelSerializer(PO,data=JO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated Successfully'})
        else:
            return Response({'Error':'Data is not Updated'})

    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JO=request.data
        PDO=ProductModelSerializer(PO,data=JO,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated Successfully'})
        else:
            return Response({'Error':'Data is not Updated'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Delete':'Data is Deleted Successfully'})