#NECESITA REVISION
from schema.models import Cliente, ClienteFisico, ClienteMoral

def delete_clientes():
    Cliente.objects.all().delete()

def run():
    delete_clientes()
