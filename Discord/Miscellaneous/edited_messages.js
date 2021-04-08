/*
Another module created by my friend, also try this out!!
*/

//Edit detection vars
var target_class = "markup-2BOw-j messageContent-2qWWxC";
var timeStamps = [];
var colored_edit_capture = "<code class='inline'><b><font color = '#3fff00' size = '2'>Before edit</b>: </font><font color = '#FF0000' size = '2'>"

//Listens for edited messages
document.body.addEventListener("DOMSubtreeModified", function (e) {
    if (e.path[1].className == target_class && timeStamps.includes(e.timeStamp) == false) {
        e.srcElement.parentElement.innerHTML = colored_edit_capture + "<b>" + e.target.__reactInternalInstance$.memoizedProps + "</b></font></code>\n" + e.target.textContent;
        timeStamps.push(e.timeStamp);
    }
});
