from django.contrib.auth.models import User
from django.test import TestCase

class TestUserPermissions(TestCase):
    def test_permission_aseguradora(self):
        user = User.objects.create_user(username='ivanalejandro', password='ivan')
        user.user_permissions = ['add_Aseguradora']
        user.save()
        user = User.objects.all().first()
        self.assertEqual(user.has_perm('add_Aseguradora'), True)
