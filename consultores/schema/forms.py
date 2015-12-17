from django import forms
from django.forms import ModelForm
from .models import Agente, Cliente, Cotizacion, CoberturaUtilizada, Poliza, Pago, SeguroAP, SeguroC, SeguroR, SeguroG, SeguroV, SeguroH, SeguroI, SeguroE, SeguroEC, SeguroT

class LoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class nuevoClienteForm(forms.ModelForm):
	class Meta:
 		model = Cliente
 		fields = ['nombre','apellidoPaterno','apellidoMaterno','email','telefonoLada','telefono','edad','sexo','rfc','calle','numeroExt',
 		'numeroInt','colonia','ciudad','estado','codigoPostal','calleFact','numeroExtFact','numeroIntFact','coloniaFact','ciudadFact'
 		,'estadoFact','codigoPostalFact']


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['costo', 'formaPago', 'aseguradora', 'archivo']

class CoberturaUtilizadaForm(forms.ModelForm):
    class Meta:
        model = CoberturaUtilizada
        fields = ['idCobertura', 'sumaAsegurada', 'deducible']

class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['idPoliza', 'noPoliza', 'primaNeta', 'fechaEmision', 'fechaInicio', 'fechaFin', 'endosoBeneficiario', 'caratulaPDF']
        # fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['idPago', 'cantidad', 'fechaPago', 'comprobante']

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


# FORMAS DE SEGUROS
class SeguroAPForm(forms.ModelForm):
	class Meta:
		model = SeguroAP
		fields = ['tipoPlan', 'marca', 'modelo', 'ano', 'version', 'transmision', 'pasajeros', 'descripcion', 'descripcion']

class SeguroCForm(forms.ModelForm):
	class Meta:
		model = SeguroC
		fields = ['marca', 'modelo', 'ano', 'transmision', 'unidad', 'pasajeros', 'descripcion']

class SeguroRForm(forms.ModelForm):
    class Meta:
        model = SeguroR
        fields = ['capacidad', 'ejes', 'descripcion']

class SeguroGForm(forms.ModelForm):
    class Meta:
        model = SeguroG
        fields = ['nombreAsegurado', 'coaseguro', 'topeCoaseguro']

class SeguroVForm(forms.ModelForm):
    class Meta:
        model = SeguroV
        fields = ['nombreAsegurado', 'edad', 'sexo', 'fumador', 'link']

class SeguroHForm(forms.ModelForm):
    class Meta:
        model = SeguroH
        fields = ['tipoVivienda', 'metrosCuadrados', 'primeraResidencia', 'calle', 'numeroExt', 'numeroInt', 'colonia', 'ciudad', 'estado', 'codigoPostal', 'capitalContinente', 'capitalContenido']

class SeguroIForm(forms.ModelForm):
    class Meta:
        model = SeguroI
        fields = ['sumaAsegurada', 'planAhorro', 'identificacion']

class SeguroEForm(forms.ModelForm):
    class Meta:
        model = SeguroE
        fields = ['nombreEmpresa', 'tipoConstruccion', 'tipoMuro', 'numeroPisos', 'numeroSotanos', 'direccion', 'numeroExt',
        'numeroInt', 'colonia', 'ciudad', 'estado', 'codigoPostal']

class SeguroECForm(forms.ModelForm):
    class Meta:
        model = SeguroEC
        fields = ['tipoEquipo', 'caracteristicas']

class SeguroTForm(forms.ModelForm):
    class Meta:
        model = SeguroT
        fields = ['tipoTrabajo', 'tipoMedio', 'bienTransportado', 'sumaAsegurada', 'ciudadOrigen', 'estadoOrigen',
        'ciudadDestino', 'estadoDestino']

class EliminarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = []
