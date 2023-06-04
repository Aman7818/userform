from django.core.mail import send_mail
from django.forms import model_to_dict
from django.shortcuts import render

from userform.forms import UserFormForm
from userform.models import UserForm
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userform.serializers import UserFormSerializer

class UserFormView(APIView):
    def get(self, request):
        form = UserFormForm()
        serialized_form = model_to_dict(form.instance)
        return Response({'form': serialized_form}, status=status.HTTP_200_OK)
    # def get(self, request):
    #     form = UserFormForm()
    #     return render(request, 'user_form.html', {'form': form})

    def post(self, request):
        serializer = UserFormSerializer(data=request.data)
        if serializer.is_valid():
            user_form = serializer.save()
            send_mail(
                'Form Submission',
                'Thank you for submitting the form.',
                'yadavaman4491@gmail.com',
                [user_form.email],
                fail_silently=False,
            )
            return Response({'message': 'Form submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormListView(APIView):
    def get(self, request):
        user_forms = UserForm.objects.all()
        serializer = UserFormSerializer(user_forms, many=True)
        return Response({'user_forms': serializer.data}, status=status.HTTP_200_OK)
