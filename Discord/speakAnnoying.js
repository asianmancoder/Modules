// This module is just ttps://github.com/asianmancoder/Modules/blob/main/Discord/annoying.js with more code.

function ok() {
    const messages = document.getElementsByClassName("markup-2BOw-j messageContent-2qWWxC");
    for(var i = 0; i < messages.length; i++) {
        window.speechSynthesis.speak(new SpeechSynthesisUtterance(messages[i].innerText));
    }
}

document.getElementsByClassName("container-3baos1")[0].innerHTML += "<button id='speakMsgHistory'>Click me for the annoying computer - speaker - guy to recite part of the message history";
document.getElementById("speakMsgHistory").onclick = ok;
