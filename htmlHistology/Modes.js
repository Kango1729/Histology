function ReadMode(form){
    [].forEach.call(document.getElementsByClassName(form),function(form){

        form.innerHTML = ReadForm(form, '#000000' )

    });
}
function ReadForm(form, Color){
    switch (Number(document.getElementById("ReadLang").value)) {
        case 1:
            output = "<font color = " + Color + ">" + form.dataset.jp + "</font>";
            break;
        case 2:
            output = "<font color = " + Color + ">" + form.dataset.eng + "</font>"
            break;
        default:
            output = "<font color = " + Color + ">" + form.dataset.jp + "&quot;" +  form.dataset.eng + "</font>&quot;";
        }
        var boolBold = {"0":1,"1":1,"2":0,"3":0,"4":0,"topic":3,"origin":2};
        var a = form.dataset.rfont
        switch (boolBold[form.dataset.rfont]) {
            case 0:
                output = output;
                break;
            case 1:
                output = "<b>" + output + "</b>";
                break;
            case 2:
                output = "<i>" + output + "</i>"
                break;
            case 3:
                output = "<b><i>" + output + "</i></b>"
            default:
        }

return output;
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
            var cor = form.dataset.jp;
            break;
            case 1:
            var ques = ""
            var cor = form.dataset.eng;
            break;
            case 2:
            var ques = form.dataset.jp;
            var cor = form.dataset.eng;
            break;
            case 3:
            var ques = form.dataset.eng;
            var cor = form.dataset.jp;
            break;
        }

        button.addEventListener("click", function(){
            check(cor, form, text.value);
        });
        form.innerHTML = "<b>"  +  ques + "</b>"
        form.insertBefore(text, null);
        form.insertBefore(button, null);
    });
}

function check(correct, form, answer){
    if(answer == correct){
        form.innerHTML = ReadForm(form, '#ff4e4e' );
    } else {
        form.innerHTML = ReadForm(form, '#ff4e4e' ) + "<font color = '0003ff'><b>×(" + answer + ")<b></font>";
    }
}
