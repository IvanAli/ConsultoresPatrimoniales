from django.shortcuts import render, render_to_response
from . import forms
from django.forms import formset_factory
from django.forms import BaseFormSet
from schema import models
from .models import Agente, Cliente, ClienteFisico, ClienteMoral, Seguro, TipoSeguro, OrdenServicio, Comparativa, Aseguradora, Cobertura, Cotizacion, CoberturaUtilizada
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from easy_pdf.views import PDFTemplateView
from . import managers
from django.forms.models import model_to_dict
# Create your views here.

"""
    AGREGAR DECORATORS - PENDIENTE
    PS: Me gusta codear en ingles
"""

# HELPER FUNCTIONS
def getUser(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None

def isAgente(user):
    return user.groups.filter(name='agente').exists()

# VIEWS
def loginView(request):
    return render(request, "schema/login.html", {})

def loginAuthentication(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_form = login_form.cleaned_data['user']
            password_form = login_form.cleaned_data['password']
            user = authenticate(username=user_form, password=password_form)
            if user is not None:
                if user.is_active:
                    # request.session['username'] = user.username
                    login(request, user)
                    return HttpResponseRedirect(reverse('schema:home'))
                else:
                    context = {'error_sessionexpired': 'Sesión expirada'}
                    return render(request, 'schema/login.html', context)
            else:
                context = {'error_wrongpassword': "Contraseña incorrecta"}
                return render(request, 'schema/login.html', context)
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/login.html', context)

def registerAgente(request):
    return HttpResponse("Work in Progress")

def home(request):
    if isAgente(request.user):
        context = {'agente': Agente.objects.get(userAgente=request.user)}
        return render(request, 'schema/home.html', context)
    else:
        print("NOT AN AGENT")

def nuevoClienteView(request):
    context = {'cliente': request.user.agente.clientes}
    return render(request, "schema/nuevoCliente.html", context)

def nuevoClienteAuth(request):
    if request.method == "POST":
        datos_form = forms.nuevoClienteForm(request.POST)
        if datos_form.is_valid():
            cliente = datos_form.save()
            request.user.agente.clientes.add(cliente)
            return HttpResponseRedirect(reverse('schema:clientes'))
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/nuevoCliente.html', context)

def clientesView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/clientes.html', context)

def infoClienteView(request, idCliente):
    context = {'cliente': Cliente.objects.get(pk=idCliente)}
    return render(request, 'schema/infocliente.html', context)

def preNuevaComparativaView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/preNuevaComparativa.html', context)

def nuevaComparativaView(request, idCliente):
    context = {
        'cliente': request.user.agente.clientes.get(pk=idCliente),
        'seguros': Seguro.objects.all(),
        'APform': forms.SeguroAPForm(),
        'Cform': forms.SeguroCForm(),
        'Rform': forms.SeguroRForm(),
        'Gform': forms.SeguroGForm(),
        'Vform': forms.SeguroVForm(),
        'Hform': forms.SeguroHForm(),
        'Iform': forms.SeguroIForm(),
        'Eform': forms.SeguroEForm(),
        'ECform': forms.SeguroECForm(),
        'Tform': forms.SeguroTForm(),
        'coberturas': Cobertura.objects.all(),
        'coberturasAP': Cobertura.objects.filter(seguro__pk='AP'),
        'coberturasC': Cobertura.objects.filter(seguro__pk='C'),
        'coberturasR': Cobertura.objects.filter(seguro__pk='R'),
        'coberturasG': Cobertura.objects.filter(seguro__pk='G'),
        'coberturasV': Cobertura.objects.filter(seguro__pk='V'),
        'coberturasH': Cobertura.objects.filter(seguro__pk='H'),
        'coberturasI': Cobertura.objects.filter(seguro__pk='I'),
        'coberturasE': Cobertura.objects.filter(seguro__pk='E'),
        'coberturasEC': Cobertura.objects.filter(seguro__pk='EC'),
        'coberturasT': Cobertura.objects.filter(seguro__pk='T'),
    }
    return render(request, 'schema/nuevaComparativa.html', context)

def nuevaComparativaAPAuth(request, idCliente):
    if request.method == 'POST':
        APform = forms.SeguroAPForm(request.POST)
        if APform.is_valid():
            return HttpResponse("it's valid yei")
        else:
            return HttpResponse("not valid fuck")


def nuevaComparativaAuth(request, idCliente):
    if request.method == "POST":
        if request.POST['tipo'] == 'AP':
            APform = forms.SeguroAPForm(request.POST)
            if APform.is_valid():
                print("valid as fuck")
                seguroComparativa = APform.save(commit=False)
                tipoSeguro = TipoSeguro(nombre=Seguro.objects.get(pk='AP'))
                tipoSeguro.save()
                seguroComparativa.tipoSeguro = tipoSeguro
                seguroComparativa.save()
                print(seguroComparativa.tipoSeguro.nombre.nombre)
                # seguroComparativa.tipoSeguro.nombre = Seguro.objects.get(pk='AP')
                # seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa.tipoSeguro)
                comparativa.save()

                checklist = request.POST.getlist('coberturaAP')
                for checked in checklist:
                    print("id cobertura:", checked)
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                comparativa.save()
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                for err in APform.errors:
                    print("error:")
                    print(err)
                return HttpResponse('Error de datos')
        if request.POST['tipo'] == 'C':
            Cform = forms.SeguroCForm(request.POST)
            if Cform.is_valid():
                seguroComparativa = Cform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='C')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaC')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'R':
            Rform = forms.SeguroRForm(request.POST)
            if Rform.is_valid():
                seguroComparativa = Rform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='R')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaR')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'G':
            print("Nombre", request.POST['nombreAsegurado'])
            print("Coaseguro", request.POST['coaseguro'])
            print("Topecoaseguro", request.POST['topeCoaseguro'])
            Gform = forms.SeguroGForm(request.POST)
            if Gform.is_valid():
                seguroComparativa = Gform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='G')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaG')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                for err in Gform.errors:
                    print("error:")
                    print(err)
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'V':
            Vform = forms.SeguroVForm(request.POST)
            if Vform.is_valid():
                seguroComparativa = Vform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='V')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaV')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'H':
            Hform = forms.SeguroHForm(request.POST)
            if Hform.is_valid():
                seguroComparativa = Hform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='H')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaH')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'I':
            Iform = forms.SeguroIForm(request.POST)
            if Iform.is_valid():
                seguroComparativa = Iform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='I')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaI')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'E':
            Eform = forms.SeguroEForm(request.POST)
            if Eform.is_valid():
                seguroComparativa = Eform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='E')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaE')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'EC':
            ECform = forms.SeguroECForm(request.POST)
            if ECform.is_valid():
                seguroComparativa = ECform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='EC')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaEC')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
        if request.POST['tipo'] == 'T':
            Tform = forms.SeguroTForm(request.POST)
            if Tform.is_valid():
                seguroComparativa = Tform.save()
                seguroComparativa.nombre = Seguro.objects.get(pk='T')
                seguroComparativa.save()
                comparativa = Comparativa(tipoSeguro=seguroComparativa)
                comparativa.save()

                checklist = request.POST.getlist('coberturaT')
                for checked in checklist:
                    comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
                ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa)
                ordenServicio.save()
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse("Forma invalida")
    # tmp
    return HttpResponse('Autenticando nueva Comparativa...')


def comparativasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/comparativas.html', context)

def comparativaClienteView(request, idComparativa):
    seguroAP = Comparativa.objects.get(pk=idComparativa).tipoSeguro.seguroAP
    print(seguroAP)
    print(seguroAP.marca)
    datosAP = forms.SeguroAPForm(data=model_to_dict(seguroAP))
    #  'datosAP': datosAP
    context = {'comparativa': Comparativa.objects.get(pk=idComparativa), 'datosAP': datosAP}
    return render(request, 'schema/comparativacliente.html', context)

def cotizacionClienteView(request, idCotizacion):
    context = {'cotizacion': Cotizacion.objects.get(pk=idCotizacion)}
    return render(request, 'schema/cotizacioncliente.html', context)

def nuevaCotizacionView(request, idComparativa):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    comparativa = Comparativa.objects.get(pk=idComparativa)
    tipo = comparativa.tipoSeguro.nombre.idSeguro

    formset = formset_factory(forms.CoberturaUtilizadaForm, max_num=20, formset=RequiredFormSet)
    cuformset = formset()
    for form in cuformset.forms:
        form.fields['idCobertura'].queryset = Cobertura.objects.filter(seguro__pk=tipo)

    coberturaUtilizadaForm = forms.CoberturaUtilizadaForm()
    coberturaUtilizadaForm.fields['idCobertura'].queryset = Cobertura.objects.filter(seguro__pk=tipo)
    context = {
        'comparativa': Comparativa.objects.get(pk=idComparativa),
        'aseguradoras': Aseguradora.objects.all(),
        'cotizacionForm': forms.CotizacionForm(),
        'coberturaUtilizadaForm': coberturaUtilizadaForm,
        'coberturas': Cobertura.objects.filter(seguro__pk=tipo),
        'formset': cuformset,
        'uploadFileForm': forms.UploadFileForm(),
    }
    return render(request, 'schema/nuevaCotizacion.html', context)

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# VALIDACION DE COBERTURAS INTRODUCIDAS PENDIENTES
def nuevaCotizacionAuth(request, idComparativa):
    # cuForm = forms.coberturaUtilizadaForm(request.POST)
    formset = formset_factory(forms.CoberturaUtilizadaForm)
    if request.method == 'POST':
        cotizacionForm = forms.CotizacionForm(request.POST, request.FILES, instance=Cotizacion())
        cuForm = forms.CoberturaUtilizadaForm(request.POST)
        cuFormset = formset(request.POST, request.FILES)
        # uploadedFileForm = forms.UploadFileForm(request.POST, request.FILES)

        if cotizacionForm.is_valid() and cuFormset.is_valid():
            """
            handle_uploaded_file(request.FILES['file'])
            fileUploaded = uploadedFileForm.save()
            """
            cotizacion = cotizacionForm.save()
            for form in cuFormset.forms:
                cobertura = form.save(commit=False)
                cobertura.cotizacion = cotizacion
                cobertura.save()
            cotizacion.comparativa = Comparativa.objects.get(pk=idComparativa)
            cotizacion.save()
            return HttpResponseRedirect(reverse('schema:comparativas'))
        else:
            for err in cotizacionForm.errors:
                print(err)
            for err in uploadedFileForm.errors:
                print(err)
            return HttpResponse("error")

    """
    cuForms = [forms.CoberturaUtilizadaForm(request.POST, prefix=str(x), instance=CoberturaUtilizada()) for x in range(0, 3)]
    if cotizacionForm.is_valid() and any([coberturaForm.is_valid() for coberturaForm in cuForms]):
        cotizacion = cotizacionForm.save()
        for coberturaForm in cuForms:
            print(coberturaForm)
            newCobertura = coberturaForm.save(commit=False)
            newCobertura.cotizacion = cotizacion
            newCobertura.save()
        cotizacion.comparativa = Comparativa.objects.get(pk=idComparativa)
        cotizacion.save()
        return HttpResponseRedirect(reverse('schema:comparativas'))
    else:
        for err in cotizacionForm.errors:
            print("error:", err)
        for element in cuForms:
            for err in element.errors:
                print("error cobertura:", err)
    """
    return HttpResponse("error")

def polizasView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/polizas.html', context)

# not working
class ComparativaPDFView(PDFTemplateView):
    template_name = "schema/pdf/comparativapdf.html"

    def get_context_data(self, **kwargs):
        return super(ComparativaPDFView, self).get_context_data(
            pagesize="A4",
            title="Comparativa",
            **kwargs
        )
