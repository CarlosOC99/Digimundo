var header = document.getElementById('header');
window.addEventListener('scroll', ()=>{
    var scroll= window.scrollY
    if(scroll>10){
        header.style.backgroundColor = 'rgb(16, 49, 65)'
    } else{
        header.style.backgroundColor = 'transparent'
    }
})

function ch(e) {
    tecla = (document.all) ? e.keyCode : e.which;

    //Tecla de retroceso para borrar, siempre la permite
    if (tecla == 8) {
        return true;
    }

    // Patron de entrada, en este caso solo acepta numeros y letras
    patron = /[A-Za-z]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}



function numb(e) {
    tecla = (document.all) ? e.keyCode : e.which;

    if (tecla == 8) {
        return true;
    }

    patron = /[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}