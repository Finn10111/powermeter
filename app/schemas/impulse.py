from .. import ma
from ..models.impulse import Impulse
from marshmallow import fields
from .namespacedSchema import NamespacedSchema


class ImpulseQuerySchema(ma.Schema):
    class Meta:
        strict = True

    timeperiod = fields.String()


class ImpulseSchema(NamespacedSchema):

    class Meta:
        strict = True
        model = Impulse
        name = "impulse"
        plural_name = "impulses"
