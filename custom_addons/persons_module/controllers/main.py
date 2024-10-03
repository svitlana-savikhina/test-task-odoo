from odoo import http
from odoo.http import request


class PersonsController(http.Controller):

    @http.route('/persons', type='http', auth="public", website=True)
    def persons_list(self):
        persons = request.env['persons'].search([], limit=5, order="id desc")
        return request.render('person_modul.templates', {
            'persons': persons
        })

    @http.route('/persons/create', auth='public', type='http', methods=['POST'], website=True)
    def create_person(self, **kwargs):
        request.env['persons'].create({
            'first_name': kwargs.get('first_name'),
            'last_name': kwargs.get('last_name'),
            'birthday': kwargs.get('birthday'),
            'sex': kwargs.get('sex'),
            'company_id': request.env.user.company_id.id,
        })
        return request.redirect('/persons')