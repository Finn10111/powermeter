from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.impulse import ImpulseSchema, ImpulseQuerySchema
from ..models.impulse import Impulse

bp = Blueprint('impulse', 'impulses', url_prefix='impulses',
               description='Operations on impulses')


@bp.route('/')
class Impulses(MethodView):

    @bp.arguments(ImpulseQuerySchema, location="query")
    @bp.response(ImpulseSchema(many=True))
    def get(self, args):
        impulses = Impulse.query.all()
        return impulses

    @bp.arguments(ImpulseSchema)
    @bp.response(ImpulseSchema, code=201)
    def post(self, new_impulse):
        db.session.add(new_impulse)
        db.session.commit()
        return new_impulse


@bp.route('/<impulse_id>')
class ImpulseById(MethodView):
    @bp.response(code=204)
    def delete(self, impulse_id):
        impulse = Impulse.query.filter_by(id=impulse_id).first()
        db.session.delete(impulse)
        db.session.commit()

