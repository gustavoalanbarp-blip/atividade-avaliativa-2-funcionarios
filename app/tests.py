from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from .models import Funcionario

class CrudTests(TestCase):
    dados = {'nome': 'Pessoa de Teste', 'cpf': '000.000.000-00',
             'email': 'teste@example.com', 'remuneracao': '2500.00'}

    def test_ciclo_completo(self):
        self.assertContains(self.client.get(reverse('lista_funcionarios')), 'Nenhum funcionário')
        self.assertRedirects(self.client.post(reverse('form_funcionario'), self.dados), reverse('lista_funcionarios'))
        fun = Funcionario.objects.get()
        self.assertContains(self.client.get(reverse('lista_funcionarios')), fun.nome)
        self.assertContains(self.client.get(reverse('listar_funcionario', args=[fun.pk])), fun.email)
        self.assertEqual(self.client.get(reverse('editar_funcionario', args=[fun.pk])).status_code, 200)
        dados = {**self.dados, 'nome': 'Nome Alterado', 'remuneracao': '3100.50'}
        self.assertRedirects(self.client.post(reverse('editar_funcionario', args=[fun.pk]), dados), reverse('lista_funcionarios'))
        fun.refresh_from_db()
        self.assertEqual(fun.nome, 'Nome Alterado')
        self.assertEqual(fun.remuneracao, Decimal('3100.50'))
        url = reverse('remover_funcionario', args=[fun.pk])
        self.assertContains(self.client.get(url), 'Confirmar exclusão')
        self.assertTrue(Funcionario.objects.filter(pk=fun.pk).exists())
        self.assertRedirects(self.client.post(url), reverse('lista_funcionarios'))
        self.assertFalse(Funcionario.objects.exists())

    def test_invalidos_nao_persistem(self):
        for campo, valor in [('nome',''), ('cpf',''), ('email','invalido'), ('remuneracao','1000000.00')]:
            response = self.client.post(reverse('form_funcionario'), {**self.dados, campo: valor})
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.context['form'].errors)
            self.assertFalse(Funcionario.objects.exists())

    def test_ids_inexistentes(self):
        for nome in ['listar_funcionario', 'editar_funcionario', 'remover_funcionario']:
            self.assertEqual(self.client.get(reverse(nome, args=[999])).status_code, 404)

    def test_csrf(self):
        client = Client(enforce_csrf_checks=True)
        self.assertEqual(client.post(reverse('form_funcionario'), self.dados).status_code, 403)
        fun = Funcionario.objects.create(**self.dados)
        self.assertEqual(client.post(reverse('remover_funcionario', args=[fun.pk])).status_code, 403)
        self.assertTrue(Funcionario.objects.filter(pk=fun.pk).exists())
