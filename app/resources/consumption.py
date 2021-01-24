from .. import db
import datetime
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.consumption import ConsumptionSchema, ConsumptionQuerySchema
from ..models.impulse import Impulse
from sqlalchemy.sql import func

bp = Blueprint('consumption', 'consumptions', url_prefix='consumption',
               description='Operations on consumptions')


@bp.route('/')
class Consumptions(MethodView):
    @bp.arguments(ConsumptionQuerySchema, location="query")
    @bp.response(ConsumptionSchema(many=False))
    def get(self, args):
        if "timeperiod" in args:
            timeperiod = int(args['timeperiod'])
            filterdate = datetime.datetime.now() - datetime.timedelta(seconds=timeperiod)
            consumption = db.session.query(func.sum(Impulse.power)).filter(Impulse.created_at >= filterdate).first()[0]
        else:
            consumption = db.session.query(func.sum(Impulse.power)).first()[0]
        return {'consumption': consumption}
