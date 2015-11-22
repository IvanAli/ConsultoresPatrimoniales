from django.shortcuts import render, render_to_response
from . import forms
from django.forms import formset_factory
from django.forms import BaseFormSet
from schema import models
from .models import Agente, Administrador, Cliente, ClienteFisico, ClienteMoral, Poliza, Pago, Seguro, AreaTramites, TipoSeguro, OrdenServicio, Comparativa, Aseguradora, Contacto, Cobertura, Cotizacion, CoberturaUtilizada
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from easy_pdf.views import PDFTemplateView
from . import managers
from django.forms.models import model_to_dict
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from datetime import datetime, timedelta
from django.template import loader
# Create your views here.

# from django.conf.settings import PROJECT_ROOT


# HELPER FUNCTIONS
def getUser(username):
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None

def isAgente(user):
    return user.groups.filter(name='agente').exists()

def whichUser(user):
    groupID = 0;
    if user.groups.filter(name="admin").exists():
        groupID = 2
    elif user.groups.filter(name='agente').exists():
        groupID = 1
    return groupID

# VIEWS
@csrf_protect
def loginView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('schema:home'))
    else:
        context = {}
        return render(request, "schema/login.html", context)

@csrf_protect
def logoutView(request):
    logout(request)
    context = {'message_logoutsuccess': "¡Has salido exitosamente!"}
    return render(request, "schema/login.html", context)

@csrf_protect
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
                context = {'error_wrongpassword': "Usuario o contraseña incorrectos"}
                return render(request, 'schema/login.html', context)
        else:
            context = {'error_missingfields': "Campos sin llenar"}
            return render(request, 'schema/login.html', context)

def registerAgente(request):
    return HttpResponse("Work in Progress")

@login_required(redirect_field_name='')
def home(request):
    if whichUser(request.user) == 1:
        agente = Agente.objects.get(userAgente=request.user)
        ordenes = agente.ordenservicio_set.all()
        lastTwoMonths = datetime.today() - timedelta(days=60)
        clienteReciente = agente.clientes.all().order_by('-pk')[0]
        # filter polizas vencidas and activas
        polizasVencidas = Poliza.objects.filter(ordenServicio__agente=agente, fechaFin__lt=datetime.now())
        polizasActivas = Poliza.objects.filter(ordenServicio__agente=agente, fechaFin__gte=datetime.now())
        # filter polizas from the last two months
        # polizas = Poliza.objects.filter(ordenServicio__agente=agente)
        polizas = Poliza.objects.filter(ordenServicio__agente=agente, fechaFin__gte=lastTwoMonths)
        cotizacionesSinPoliza = Cotizacion.objects.filter(comparativa__ordenServicio__agente=agente, elegida=True, poliza=None)
        comparativasPendientes = Comparativa.objects.filter(ordenServicio__agente=agente, fechaConclusion=None)
        for poliza in polizas:
            print(poliza)
        context = {
            'agente': agente,
            'ordenes': ordenes,
            'polizas': polizas,
            'polizasVencidas': polizasVencidas,
            'polizasActivas': polizasActivas,
            'clienteReciente': clienteReciente,
            'comparativasPendientes': comparativasPendientes,
            'cotizacionesSinPoliza': cotizacionesSinPoliza,
        }
        return render(request, 'schema/home.html', context)
    elif whichUser(request.user) == 2:
        context = {'agente': Administrador.objects.get(userAdmin=request.user)}
        return render(request, 'schema/homeAdmin.html', context)

@login_required(redirect_field_name='')
def nuevoClienteView(request):
    context = {'cliente': request.user.agente.clientes}
    return render(request, "schema/nuevoCliente.html", context)

@login_required(redirect_field_name='')
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

@login_required(redirect_field_name='')
def clientesView(request):
    if whichUser(request.user) == 1:
        context = {'clientes': request.user.agente.clientes}
        return render(request, 'schema/clientes.html', context)
    elif whichUser(request.user) == 2:
        context = {'clientes': Cliente.objects.all()}
        return render(request, 'schema/clientesAdmin.html', context)


@login_required(redirect_field_name='')
def infoClienteView(request, idCliente):
    context = {'cliente': Cliente.objects.get(pk=idCliente)}
    return render(request, 'schema/infocliente.html', context)

@login_required(redirect_field_name='')
def preNuevaComparativaView(request):
    context = {'clientes': request.user.agente.clientes}
    return render(request, 'schema/preNuevaComparativa.html', context)

@login_required(redirect_field_name='')
def seleccionClienteView(request, context_type):
    context = {
        'clientes': request.user.agente.clientes,
        'context_type': context_type,
    }
    return render(request, 'schema/seleccionCliente.html', context)

@login_required(redirect_field_name='')
def seleccionOrdenServicioView(request):
    context = {
        'ordenes': OrdenServicio.objects.filter(agente=request.user.agente).exclude(comparativa__fechaEnvioTramite=None),
    }
    return render(request, 'schema/seleccionOrdenServicio.html', context)

def nuevaPolizaView(request, idOrdenServicio):
    # check if direccion fields have been filled in
    ordenServicio = OrdenServicio.objects.get(pk=idOrdenServicio)
    cliente = ordenServicio.cliente
    allFilledIn = cliente.rfc and cliente.calle and cliente.numeroExt and cliente.colonia and cliente.ciudad and cliente.estado and cliente.codigoPostal
    # the rest of the fields to check
    allFilledIn = allFilledIn and True
    # allFilledIn = cliente.rfc != "" and cliente.calle != "" and cliente.numeroExt is not None and cliente.colonia != "" and cliente.ciudad != "" and cliente.estado != "" and cliente.codigoPostal != ""
    if allFilledIn:
        context = {'orden': ordenServicio, 'polizaForm': forms.PolizaForm()}
        return render(request, 'schema/nuevaPoliza.html', context)
    return HttpResponse('Falta llenar direccion del cliente')

@login_required(redirect_field_name='')
def nuevaPolizaAuthView(request, idOrdenServicio):
    form = forms.PolizaForm(request.POST, request.FILES)
    if form.is_valid():
        poliza = form.save(commit=False)
        # adding other attributes probably missing
        ordenServicio = OrdenServicio.objects.get(pk=idOrdenServicio)
        poliza.ordenServicio = ordenServicio
        poliza.cotizacion = getCotizacionPreferida(ordenServicio.comparativa.pk)
        poliza.save()
        return HttpResponseRedirect(reverse('schema:polizas'))
    else:
        for err in form.errors:
            print(err)
    return HttpResponse('No success')

@login_required(redirect_field_name='')
def polizaClienteView(request, idPoliza):
    poliza = Poliza.objects.get(pk=idPoliza)
    context = {'poliza': poliza}
    return render(request, 'schema/infoPoliza.html', context)

@login_required(redirect_field_name='')
def nuevoPagoView(request, idPoliza):
    poliza = Poliza.objects.get(pk=idPoliza)
    context = {'poliza': poliza, 'pagoForm': forms.PagoForm()}
    return render(request, 'schema/nuevoPago.html', context)

@login_required(redirect_field_name='')
def nuevoPagoAuthView(request, idPoliza):
    form = forms.PagoForm(request.POST, request.FILES)
    if form.is_valid():
        pago = form.save(commit=False)
        poliza = Poliza.objects.get(pk=idPoliza)
        if Pago.objects.filter(poliza=poliza).count() == 0:
            pago.numeroPago = 1
        else:
            lastPago = Pago.objects.filter(poliza=poliza).orden_by('-numeroPago')[0]
            pago.numeroPago = lastPago + 1
        pago.poliza = poliza
        pago.save()
        return HttpResponseRedirect(reverse('schema:polizaCliente', args=[idPoliza]))
    return HttpResponse('Forma invalida')

@login_required(redirect_field_name='')
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


def saveForm(request, idCliente, filledForm, seguroPK):
    form = filledForm
    if form.is_valid():
        seguroComparativa = form.save(commit=False)
        tipoSeguro = TipoSeguro(nombre=Seguro.objects.get(pk=seguroPK))
        tipoSeguro.save()
        seguroComparativa.tipoSeguro = tipoSeguro
        seguroComparativa.save()
        comparativa = Comparativa(tipoSeguro=seguroComparativa.tipoSeguro)
        comparativa.save()
        criteria = 'cobertura' + seguroPK
        checklist = request.POST.getlist(criteria)
        for checked in checklist:
            comparativa.coberturas.add(Cobertura.objects.get(pk=checked))
        comparativa.save()
        ordenServicio = OrdenServicio(cliente=Cliente.objects.get(pk=idCliente),comparativa=comparativa, agente=request.user.agente)
        ordenServicio.save()
        return True
    return False

@login_required(redirect_field_name='')
def nuevaComparativaAuth(request, idCliente):
    if request.method == "POST":
        tipo = request.POST['tipo']
        if tipo == 'AP':
            if saveForm(request, idCliente, forms.SeguroAPForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'C':
            if saveForm(request, idCliente, forms.SeguroCForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'R':
            if saveForm(request, idCliente, forms.SeguroRForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'G':
            if saveForm(request, idCliente, forms.SeguroGForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'V':
            if saveForm(request, idCliente, forms.SeguroVForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'H':
            if saveForm(request, idCliente, forms.SeguroHForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'I':
            if saveForm(request, idCliente, forms.SeguroIForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'E':
            if saveForm(request, idCliente, forms.SeguroEForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'EC':
            if saveForm(request, idCliente, forms.SeguroECForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')
        if tipo == 'T':
            if saveForm(request, idCliente, forms.SeguroTForm(request.POST), tipo):
                return HttpResponseRedirect(reverse('schema:comparativas'))
            else:
                return HttpResponse('Forma ' + tipo + ' invalida')

@login_required(redirect_field_name='')
def comparativasView(request):
    if whichUser(request.user) == 1:
        context = {'clientes': request.user.agente.clientes}
        return render(request, 'schema/comparativas.html', context)
    elif whichUser(request.user) == 2:
        context = {'agentes': Agente.objects.all()}
        return render(request, 'schema/comparativasAdmin.html', context)

def modelFieldExists(model, field):
    return hasattr(model, field)

def getDatosSeguro(idComparativa):
    comparativa = Comparativa.objects.get(pk=idComparativa)
    tipo = comparativa.tipoSeguro.nombre.pk
    if tipo == 'AP':
        return forms.SeguroAPForm(data=model_to_dict(comparativa.tipoSeguro.seguroAP))
    if tipo == 'C':
        return forms.SeguroCForm(data=model_to_dict(comparativa.tipoSeguro.seguroC))
    if tipo == 'R':
        return forms.SeguroRForm(data=model_to_dict(comparativa.tipoSeguro.seguroR))
    if tipo == 'G':
        return forms.SeguroGForm(data=model_to_dict(comparativa.tipoSeguro.seguroG))
    if tipo == 'V':
        return forms.SeguroVForm(data=model_to_dict(comparativa.tipoSeguro.seguroV))
    if tipo == 'H':
        return forms.SeguroHForm(data=model_to_dict(comparativa.tipoSeguro.seguroH))
    if tipo == 'I':
        return forms.SeguroAPForm(data=model_to_dict(comparativa.tipoSeguro.seguroI))
    if tipo == 'E':
        return forms.SeguroEForm(data=model_to_dict(comparativa.tipoSeguro.seguroE))
    if tipo == 'EC':
        return forms.SeguroECForm(data=model_to_dict(comparativa.tipoSeguro.seguroEC))
    if tipo == 'T':
        return forms.SeguroTForm(data=model_to_dict(comparativa.tipoSeguro.seguroT))

@login_required(redirect_field_name='')
def comparativaClienteView(request, idComparativa):
    context = {'comparativa': Comparativa.objects.get(pk=idComparativa), 'datos': getDatosSeguro(idComparativa)}
    return render(request, 'schema/comparativacliente.html', context)

def cotizacionClienteView(request, idCotizacion):
    context = {'cotizacion': Cotizacion.objects.get(pk=idCotizacion)}
    return render(request, 'schema/cotizacioncliente.html', context)

@login_required(redirect_field_name='')
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
@login_required(redirect_field_name='')
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
            return HttpResponseRedirect(reverse('schema:comparativaCliente', args=[idComparativa]))
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

def marcarComparativaConcluidaView(request, idComparativa):
    comparativa = Comparativa.objects.get(pk=idComparativa)
    if comparativa.fechaConclusion == None:
        comparativa.fechaConclusion = datetime.now()
    else:
        comparativa.fechaConclusion = None
    comparativa.save()
    return HttpResponseRedirect(reverse('schema:comparativaCliente', args=[idComparativa]))

def marcarCotizacionPreferidaView(request, idCotizacion):
    cotizacion = Cotizacion.objects.get(pk=idCotizacion)
    idComparativa = cotizacion.comparativa.pk
    comparativa = Comparativa.objects.get(pk=idComparativa)
    for cot in comparativa.cotizacion_set.all():
        if cot.pk is not cotizacion.pk:
            cot.elegida = False
            cot.save()
    cotizacion.elegida = not cotizacion.elegida
    cotizacion.save()
    return HttpResponseRedirect(reverse('schema:cotizacionCliente', args=[idCotizacion]))

def sendEmail(subject, message, fromEmail, toEmail):
    try:
        mail = EmailMessage(subject, message, fromEmail, toEmail)
        mail.send()
        return True
    except Exception as e:
        print(e)
        return False

def sendEmailAlternative(subject, textMessage, htmlMessage, fromEmail, toEmail):
    try:
        mail = EmailMultiAlternatives(subject, textMessage, fromEmail, toEmail)
        mail.attach_alternative(htmlMessage, 'text/html')
        mail.send()
        return True
    except Exception as e:
        print(e)
        return False

def sendEmailAlternativeWithAttachment(subject, textMessage, htmlMessage, fromEmail, toEmail, attachment, contentType):
    try:
        mail = EmailMultiAlternatives(subject, textMessage, fromEmail, toEmail)
        mail.attach_alternative(htmlMessage, 'text/html')
        mail.attach(attachment.name, attachment.read(), contentType)
        mail.send()
        return True
    except Exception as e:
        print(e)
        return False

def sendEmailWithAttachment(subject, message, fromEmail, toEmail, attachment, contentType):
    try:
        mail = EmailMessage(subject, message, fromEmail, toEmail)
        mail.attach(attachment.name, attachment.read(), contentType)
        mail.send()
        return True
    except Exception as e:
        print(e)
        return False

def enviarComparativaView(request, idComparativa):
    # file_ = open('C:/Users/Ivan/Consultores/consultores/django-storages.txt')
    comparativa = Comparativa.objects.get(pk=idComparativa)
    cliente = comparativa.ordenServicio.cliente
    seguro = comparativa.tipoSeguro.nombre
    agente = comparativa.ordenServicio.agente

    if cliente.email is None or cliente.email == "":
        return HttpResponse('El cliente no tiene email')
    else:
        subject = "Lista de cotizaciones para su seguro de " + seguro.nombre
        htmlMessage = loader.render_to_string(
            'schema/email/enviocomparativa.html',
            {
                'agente': agente,
                'cliente': cliente,
                'comparativa': comparativa,
                'seguroNombre': seguro,
                'datos': getDatosSeguro(idComparativa),
                'coberturas': Cobertura.objects.filter(seguro__pk=seguro.pk),
            }
        )
        message = "Un saludo"
        if sendEmailAlternative(subject, message, htmlMessage, 'ivanali@outlook.com', [cliente.email]):
            comparativa.fechaEnvioCliente = datetime.now()
            comparativa.save()
            return HttpResponse('Email enviado exitosamente!')
    return HttpResponse('no exito')

def getCotizacionPreferida(idComparativa):
    comparativa = Comparativa.objects.get(pk=idComparativa)
    for cotizacion in comparativa.cotizacion_set.all():
        if cotizacion.elegida:
            return cotizacion

@login_required(redirect_field_name='')
def enviarCotizacionTramitesView(request, idComparativa):
    comparativa = Comparativa.objects.get(pk=idComparativa)
    cliente = comparativa.ordenServicio.cliente
    agente = comparativa.ordenServicio.agente
    seguro = comparativa.tipoSeguro.nombre

    if getCotizacionPreferida(idComparativa) is not None:
        archivo = cotizacionElegida.archivo
        if AreaTramites.objects.count() > 0:
            encargadosList = []
            emailList = []
            for tramites in AreaTramites.objects.all():
                emailList.append(tramites.email)
            subject = 'Datos de póliza a tramitar'
            message = 'Envío datos de póliza a tramitar para cliente ' + cliente.nombre + " " + cliente.apellidoPaterno + " " + cliente.apellidoMaterno
            htmlMessage = loader.render_to_string(
                'schema/email/enviodatospoliza.html',
                {
                    'agente': agente,
                    'cliente': cliente,
                    'comparativa': comparativa,
                    'seguroNombre': seguro,
                    'datos': getDatosSeguro(idComparativa),
                    'cotizacionElegida': cotizacionElegida,
                    'coberturas': Cobertura.objects.filter(seguro__pk=seguro.pk),
                }
            )
            if sendEmailAlternativeWithAttachment(subject, message, htmlMessage, 'ivanali@outlook.com', emailList, archivo, 'application/pdf'):
                comparativa.fechaEnvioTramite = datetime.now()
                comparativa.save()
                return HttpResponse('Email enviado exitosamente!')
        else:
            return HttpResponse('No hay emails de area de tramites registrados')
    else:
        return HttpResponse('Favor de seleccionar una cotizacion preferida')

@login_required(redirect_field_name='')
def polizasView(request):
    if whichUser(request.user) == 1:
        context = {'clientes': request.user.agente.clientes}
        return render(request, 'schema/polizas.html', context)
    elif whichUser(request.user) == 2:
        context = {'agentes': Agente.objects.all()}
        return render(request, 'schema/polizasAdmin.html', context)

@login_required(redirect_field_name='')
def agentesView(request):
    if whichUser(request.user) == 1:
        return HttpResponse("No autorizado")
    elif whichUser(request.user) == 2:
        context = {'agentes': Agente.objects.all()}
        return render(request, 'schema/agentesAdmin.html', context)

@login_required(redirect_field_name='')
def aseguradorasView(request):
    if whichUser(request.user) == 1:
        return HttpResponse("No autorizado")
    elif whichUser(request.user) == 2:
        context = {
            'aseguradoras': Aseguradora.objects.all(),
            'contactos': Contacto.objects.all(),
        }
        return render(request, 'schema/aseguradorasAdmin.html', context)

@login_required(redirect_field_name='')
def segurosView(request):
    if whichUser(request.user) == 1:
        return HttpResponse("No autorizado")
    elif whichUser(request.user) == 2:
        context = {'range': range(50)}
        return render(request, 'schema/segurosAdmin.html', context)


# not working
# class ComparativaPDFView(PDFTemplateView):
#     template_name = "schema/pdf/comparativapdf.html"

#     def get_context_data(self, **kwargs):
#         return super(ComparativaPDFView, self).get_context_data(
#             pagesize="A4",
#             title="Comparativa",
#             **kwargs
#         )
