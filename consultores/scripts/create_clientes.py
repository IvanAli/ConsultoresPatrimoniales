from schema.models import Cliente, ClienteFisico, ClienteMoral

def create_clientes():
    cf1 = ClienteFisico(nombre="Ivan Alejandro", apellidoPaterno="Soto",
    apellidoMaterno="Velazquez", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
    telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
    colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro",
    codigoPostal="12345", calleFact="Jesus Oviedo", numeroExtFact=106, numeroIntFact=103,
    coloniaFact="Villas del Tecnologico", ciudadFact="Queretaro", estadoFact="Queretaro")

    cf2 = ClienteFisico(nombre="Alejandro Ivan", apellidoPaterno="Velazquez",
    apellidoMaterno="Soto", edad=20, sexo="M", rfc="SOVI", email="ivanali@outlook.com",
    telefonoLada="644", telefono="1421909", calle="Jesús Oviedo", numeroExt=106, numeroInt=33,
    colonia="Villas del Tecnológico", ciudad="Santiago de Querétaro", estado="Querétaro",
    codigoPostal="12345", calleFact="Jesus Oviedo", numeroExtFact=106, numeroIntFact=103,
    coloniaFact="Villas del Tecnologico", ciudadFact="Queretaro", estadoFact="Queretaro")

    cf3 = ClienteFisico(nombre="Foolanito", apellidoPaterno="Barrera",
    apellidoMaterno="Nope", edad=5, sexo="M", rfc="SOVI", email="foobar@foo.bar",
    telefonoLada="123", telefono="6543642", calle="Rainbow", numeroExt=678,
    colonia="Los foolanos", ciudad="Santiago de Querétaro", estado="Querétaro",
    codigoPostal="12345", calleFact="Rainbow", numeroExtFact=678,
    coloniaFact="Los foolanos", ciudadFact="Queretaro", estadoFact="Queretaro")

    cf1.save()
    cf2.save()
    cf3.save()

def run():
    create_clientes()
