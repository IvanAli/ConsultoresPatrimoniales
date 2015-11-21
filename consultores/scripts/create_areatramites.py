from schema.models import AreaTramites

def create_area_tramites():
    AreaTramites.objects.all().delete()
    a = AreaTramites(encargado='Ivan Alejandro Soto Velazquez', email='ivanali@outlook.com')
    a.save()

def run():
    create_area_tramites()
