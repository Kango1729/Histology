function ReadMode(form){
    [].forEach.call(document.getElementsByClassName(form),function(form){
        switch (Number(document.getElementById("ReadLang").value)) {
            case 1:
                form.innerHTML = "<b>" + form.dataset.answer + "</b>"
                break;
            case 2:
                form.innerHTML = "<b>" + form.dataset.eng + "</b>"
                break;
            default:
            form.innerHTML = "<b>" + form.dataset.answer + "  (" +form.dataset.eng + ") </b>"

        }
    });
}
function QuestMode (form){
    [].forEach.call(document.getElementsByClassName(form), function(form){
        form.innerHTML =""
        var text = document.createElement("input");
        text.type = "text";

        var button = document.createElement("input");
        button.type = "button";
        button.value = " ";

        button.addEventListener("click", function(){
            check(form.dataset.answer, form, text);
        });

        form.insertBefore(text, null);
        form.insertBefore(button, null);
    });
}
function check(answer, form, text){

    if(text.value == answer){
        form.innerHTML = "<font color = '#ff4e4e'><b>" + text.value + "<b></font>";
    } else {
        form.innerHTML = "<font color = '#ff4e4e'><b>" + answer + "<b></font>" + "   not<font color = '#0003ff'><b>(" + text.value + ")<b></font>";
    }
}
