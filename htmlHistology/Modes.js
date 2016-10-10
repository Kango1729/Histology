function ReadMode(form){
    [].forEach.call(document.getElementsByClassName(form),function(form){

        form.innerHTML = ReadForm(form, '#000000' );

    });
}
function ReadForm(form, Color){
        var boolShow = {"0":3,"1":3,"2":3,"3":0,"4":0,"topic":4,"origin":4,"otherjp":1,"othereng":2}
        switch (boolShow[form.dataset.rfont]) {
            case 0:
                switch (Number(document.getElementById("ReadLang").value)) {
                    case 0:
                        show = form.dataset.jp;
                        break;
                    case 1:
                        show = form.dataset.jp;
                        break;
                    case 2:
                        show = form.dataset.eng;
                        break;
                }
                break;
            case 1:
                show = form.dataset.jp;
                break;
            case 2:
                show = form.dataset.eng;
                break;
            case 3:
                switch (Number(document.getElementById("ReadLang").value)) {
                    case 0:
                        show = form.dataset.jp + "&quot;" +  form.dataset.eng + "&quot;";
                        break;
                    case 1:
                        show = form.dataset.jp;
                        break;
                    case 2:
                        show = form.dataset.eng;
                        break;
                }
                break;
            case 4:
                show = form.dataset.jp + "&quot;" +  form.dataset.eng + "&quot;";
                break;
            default:
                show = form.dataset.jp
        }
        output = "<font color = " + Color + ">" + show + "</font>";

        var boolBold = {"0":1,"1":1,"2":0,"3":0,"4":0,"topic":3,"origin":2,"otherjp":0,"othereng":0};
        switch (boolBold[form.dataset.rfont]) {
            case 0:
            	output = output;
            break;
            case 1:
                output = "<b>" + output + "</b>";
                break;
            case 2:
                output = "<i>" + output + "</i>";
                break;
            case 4:
                output = "<i><b>" + output + "</b></i>";
        }

return output;
}

function QuestMode (form){

    [].forEach.call(document.getElementsByClassName(form), function(form){
    	var boolHide = {"0":0,"1":1,"2":0,"3":1,"4":0,"topic":0,"origin":0,"otherjp":0,"othereng":0};
    	if (boolHide[form.dataset.rfont] == 1){
        	form.innerHTML ="";
        	var text = document.createElement("input");
        	text.type = "text";
        	text.size = "8"

        	var button = document.createElement("input");
        	button.type = "button";
        	button.value = " ";
        	Questlang = Number(document.getElementById("QuestLang").value);
        	switch(Questlang) {
            	case 0:
            		var ques = "";
            		var cor = form.dataset.jp;
            	break;
            	case 1:
            		var ques = "";
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

        	button.addEventListener("click",function(){check(cor, form, text.value);
        	});
        	form.innerHTML = "<b>"  +  ques + "</b>";
        	form.insertBefore(text, null);
        	form.insertBefore(button, null);
        }
    });
}

function check(correct, form, answer){
    if(answer == correct){
        form.innerHTML = ReadForm(form, '#ff4e4e' );
    } else {
        form.innerHTML = ReadForm(form, '#ff4e4e' ) + "<font color = '0003ff'><b>  ×(" + answer + ")<b></font>";
    }
}
