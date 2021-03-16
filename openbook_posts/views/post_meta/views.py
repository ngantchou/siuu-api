from django.db import transaction
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _

from openbook_moderation.permissions import IsNotSuspended


class PostMeta(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)

    def put(self, request, post_uuid):
        request_data = request.data.dict()
        request_data['post_uuid'] = post_uuid

        serializer = AddPostMetaSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        user = request.user
        post_uuid = data.get('post_uuid')
        is_png = data.get('is_png')
        is_svg = data.get('is_svg')
        is_font_color_white = data.get('is_font_color_white')
        image_path = data.get('image_path')
        is_color = data.get('is_color')

        with transaction.atomic():
            user.add_media_to_post_with_uuid(post_uuid=post_uuid, file=file, order=order)

        return Response({
            'message': _('Media added successfully to post')
        }, status=status.HTTP_200_OK)

