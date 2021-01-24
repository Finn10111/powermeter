from .. import ma
from marshmallow import fields


class ConsumptionQuerySchema(ma.Schema):
    class Meta:
        strict = True

    timeperiod = fields.String()


class ConsumptionSchema(ma.Schema):
    consumption = fields.Number()
