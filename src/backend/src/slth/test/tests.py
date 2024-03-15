from ..tests import ServerTestCase
from ..serializer import Serializar, LinkField
from .views import VisualizarPessoa

class ApiTestCase(ServerTestCase):
    def test_form(self):
        self.debug = True
        self.assert_model_count('auth.user', 0)
        self.assert_model_count('auth.group', 0)
        data = dict(
            username='brenokcc', email='brenokcc@yahoo.com.br',
            groups__0='', groups__0__name='A', groups__0__permissions='',
            groups__1='', groups__1__name='B', groups__1__permissions=''
        )
        self.post('/api/add-user/', data)
        self.assert_model_count('auth.user', 1)
        self.assert_model_count('auth.group', 2)
        self.get('/api/list-users/')
        self.get('/api/view-user/1/')

    def test_json(self):
        self.debug = True
        self.assert_model_count('auth.user', 0)
        self.assert_model_count('auth.group', 0)
        data = dict(
            username='brenokcc', email='brenokcc@yahoo.com.br',
            groups=[dict(name='A'), dict(name='B')]
        )
        self.post('/api/add-user/', json=data)
        self.assert_model_count('auth.user', 1)
        self.assert_model_count('auth.group', 2)
        self.get('/api/list-users/')
        user = self.objects('auth.user').first()
        self.get('/api/view-user/{}/'.format(user.pk))
        self.post('/api/login/', json=dict(username='brenokcc', password='213'))
        user.set_password('123')
        user.save()
        self.post('/api/login/', json=dict(username='brenokcc', password='123'))

    def test_serialization(self):
        juca = self.objects('test.pessoa').create(nome='Juca da Silva')
        cidade = self.objects('test.cidade').create(nome='Natal', prefeito=juca)
        (
            Serializar(juca)
            .fields('id', 'nome')
            .serialize(False)
        )
        (
            Serializar(juca)
            .fieldset('Dados Gerais', ('id', 'nome'))
            .serialize(False)
        )
        (
            Serializar(cidade)
            .fieldset('Dados Gerais', ('id', 'nome'), LinkField('prefeito', VisualizarPessoa))
            .fieldset('Prefeito', ('id', 'nome'), relation='prefeito')
            .serialize(True)
        )

        