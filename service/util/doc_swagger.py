from flask_restplus import fields

from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'usuario': fields.String(required=True, description="Usuário a ser verificado")})
