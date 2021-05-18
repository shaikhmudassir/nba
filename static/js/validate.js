/* Validation Setup Start */
function showPopup(message){
    document.getElementById("pop-up").style.display= 'block';
    document.getElementById("pop-up-message").innerText = message;
}
function hidePopup(){
    document.getElementById("pop-up").style.display= 'none';
}
function hideNback(){
    document.getElementById("pop-up").style.display= 'none';
    window.history.back()
}
if(document.getElementById('isServerSite').value == 'True'){
    showPopup(document.getElementById('popup-message').value);
    document.getElementsByTagName('button')[0].removeAttribute('onclick')
    document.getElementsByTagName('button')[0].setAttribute('onclick','hideNback();')
}
/* Setup End */



