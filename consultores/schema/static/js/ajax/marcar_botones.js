function marcar_boton(url, id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById(id).innerHTML = xhttp.responseText;
        }
    };
    xhttp.open('GET', url, true);
    xhttp.send();
}

function enviarCliente(url, id) {
    marcar_boton(url, id);
}

function enviarTramites(url, id) {
    marcar_boton(url, id);
}

function marcar_boton_concluida(url, id, envioClienteId, envioTramiteId, nuevaCotizacionId) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(xhttp.readyState == 4 && xhttp.status == 200) {
            envioClienteBtn = document.getElementById(envioClienteId);
            envioTramiteBtn = document.getElementById(envioTramiteId);
            nuevaCotizacionBtn = document.getElementById(nuevaCotizacionId);
            document.getElementById(id).innerHTML = xhttp.responseText;
            console.log(envioTramiteBtn.innerHTML)
            var isEnvioClienteDisabled = envioClienteBtn.getAttribute('disabled')
            var isEnvioTramiteDisabled = envioClienteBtn.getAttribute('disabled')
            // console.log("ENVIO CLIENTE: " + isEnvioClienteDisabled)
            if(isEnvioClienteDisabled == null || isEnvioTramiteDisabled == null) {
                envioClienteBtn.setAttribute("disabled","disabled");
                envioTramiteBtn.setAttribute("disabled","disabled");
                nuevaCotizacion.removeAttribute("disabled");
                console.log("both disabled");
            }
            else {
                envioClienteBtn.removeAttribute("disabled");
                envioTramiteBtn.removeAttribute("disabled");
                nuevaCotizacion.setAttribute("disabled", "disabled");
                console.log("not disabled");
            }
        }
    };
    xhttp.open('GET', url, true);
    xhttp.send();
}

function init_disabled_marking(fechaConclusion, concluidaId, envioClienteId, envioTramiteId, nuevaCotizacionId) {
    concluidaButton = document.getElementById(concluidaId);
    envioClienteBtn = document.getElementById(envioClienteId);
    envioTramiteBtn = document.getElementById(envioTramiteId);
    nuevaCotizacionBtn = document.getElementById(nuevaCotizacionId);
    console.log("fecha de conclusion: " + fechaConclusion);
    if(fechaConclusion != "None") {
        envioClienteBtn.removeAttribute("disabled");
        envioTramiteBtn.removeAttribute("disabled");
        nuevaCotizacionBtn.setAttribute("disabled", "disabled");
        concluidaButton.innerHTML = "Marcar como no concluida";
    }
    else {
        envioClienteBtn.setAttribute("disabled", "disabled");
        envioTramiteBtn.setAttribute("disabled", "disabled");
        nuevaCotizacionBtn.removeAttribute("disabled");
        concluidaButton.innerHTML = "Marcar como concluida";
    }
}

window.onload = function() {
    // init_disabled_marking(null, 'concluida', 'envioCliente', 'envioTramite', 'nuevaCotizacion');
}
