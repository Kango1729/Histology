function ReadMode(form){
    [].forEach.call(document.getElementsByClassName(form),function(form){
        switch (Number(document.getElementById("ReadLang").value)) {
            case 1:
                form.innerHTML = "<b>" + form.dataset.jp + "</b>"
                break;
            case 2:
                form.innerHTML = "<b>" + form.dataset.eng + "</b>"
                break;
            default:
            form.innerHTML = "<b>" + form.dataset.jp + " &quot;" +form.dataset.eng + "&quot; </b>"

        }
    });
}
function QuestMode (form){
    [].forEach.call(document.getElementsByClassName(form), function(form){
        form.innerHTML =""
        var text = document.createElement("input");
        text.type = "text";
        text.size = "8"

        var button = document.createElement("input");
        button.type = "button";
        button.value = " ";
        Questlang = Number(document.getElementById("QuestLang").value)
        switch
        (Questlang) {
            case 0:
            var ques = ""
            var ans = form.dataset.jp;
            break;
            case 1:
            var ques = ""
            var ans = form.dataset.eng;
            break;
            case 2:
            var ques = form.dataset.jp;
            var ans = form.dataset.eng;
            break;
            case 3:
            var ques = form.dataset.eng;
            var ans = form.dataset.jp;
            break;
        }

        button.addEventListener("click", function(){
            check(ans, form, text);
        });
        form.innerHTML = "<b>"  +  ques + "</b>"
        form.insertBefore(text, null);
        form.insertBefore(button, null);
    });
}
function check(answer, form, text){

    if(text.value == answer){
        form.innerHTML = "<font color = '#ff4e4e'><b>" + text.value + "<b></font>";
    } else {
        form.innerHTML = "<font color = '#ff4e4e'><b>" + answer + "<b></font>" + "   <font color = '#0003ff'><b>not(" + text.value + ")<b></font>";
    }
}
