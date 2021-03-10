from django.conf import settings
from django.core.validators import FileExtensionValidator
from generic_relations.relations import GenericRelatedField
from rest_framework import serializers
from video_encoding.models import Format

from openbook_common.serializers_fields.request import RestrictedImageFileSizeField, RestrictedFileSizeField
from openbook_posts.validators import post_uuid_exists, post_reaction_id_exists


class AddPostMetaSerializer(serializers.Serializer):
    post_uuid = serializers.UUIDField(
        validators=[post_uuid_exists],
        required=True,
    )
    order = serializers.IntegerField(required=False)


class GetPostMetaSerializer(serializers.Serializer):
    post_uuid = serializers.UUIDField(
        validators=[post_uuid_exists],
        required=True,
    )
