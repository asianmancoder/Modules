function ok() {
    const messages = document.getElementsByClassName("markup-2BOw-j messageContent-2qWWxC");
    for(var i = 0; i < messages.length; i++) {
        window.speechSynthesis.speak(new SpeechSynthesisUtterance(messages[i].innerText)); // Annoying
    }
}
