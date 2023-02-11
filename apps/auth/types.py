import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphene_django.utils import camelize
from .connections import UserConnection
from .exceptions import WrongUsage
from .filters import SEUserFilter
from .models import SEUser
from .settings import graphql_auth_settings as app_settings

class UserNode(DjangoObjectType):
    class Meta:
        model = SEUser
        filterset_class = SEUserFilter
        interfaces = (graphene.relay.Node,)
        skip_registry = True

    pk = graphene.Int()
    archived = graphene.Boolean()
    verified = graphene.Boolean()
    secondary_email = graphene.String()

    def resolve_pk(self, info):
        return self.pk

    def resolve_archived(self, info):
        return self.status.archived

    def resolve_verified(self, info):
        return self.status.verified

    def resolve_secondary_email(self, info):
        return self.status.secondary_email

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.select_related("status")
