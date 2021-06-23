    var epilepsy="אין";
    var downSyndrom="אין";
    var muscleDystrophy="אין";
    var heartProblem="אין";
    var noProblem="";
    var walkProblem="";
    var selectNum="";
    var selectedYesOrNo="";

    function markCheckbox1(element){
        if (element.src.endsWith('checkbox.png'))
        {
            if (element.id=='checkbox1' || element.id=='checkbox2' || element.id=='checkbox3' || element.id=='checkbox4')
            {
                if (document.getElementById("checkbox5").src.endsWith('checkbox.png'))
                    element.src=element.src.replace('checkbox', 'checked');
                if (element.id=='checkbox1')
                    epilepsy="יש";
                if (element.id=='checkbox2')
                    downSyndrom="יש";
                if (element.id=='checkbox3')
                    muscleDystrophy="יש";
                if (element.id=='checkbox4')
                    heartProblem="יש";
            }
            else
            {
                element.src=element.src.replace('checkbox', 'checked')
                noProblem="noProblem";
             }
            if (element.id=='checkbox5')
            {
                document.getElementById("checkbox1").src=document.getElementById("checkbox1").src.replace('checked', 'checkbox');
                document.getElementById("checkbox2").src=document.getElementById("checkbox2").src.replace('checked', 'checkbox');
                document.getElementById("checkbox3").src=document.getElementById("checkbox3").src.replace('checked', 'checkbox');
                document.getElementById("checkbox4").src=document.getElementById("checkbox4").src.replace('checked', 'checkbox');
                noProblem="noProblem";
            }
        }
        else
        {
           element.src=element.src.replace('checked', 'checkbox');
        }
        toggleNextButton()
    }



    function markCheckbox2(element) {

        if (element.src.endsWith('checkbox.png'))
        {
            if (walkProblem!="")
            {
                if (walkProblem=='רק בתוך הדירה')
                    document.getElementById('checkbox6').src=document.getElementById('checkbox6').src.replace('checked','checkbox')
                if (walkProblem=='בסביבה הקרובה')
                    document.getElementById('checkbox7').src=document.getElementById('checkbox7').src.replace('checked','checkbox')
                if (walkProblem=='יכול/ה ללכת מעל 20 דקות רצוף')
                    document.getElementById('checkbox8').src=document.getElementById('checkbox8').src.replace('checked','checkbox')
                if (walkProblem=='לא יכול/ה ללכת')
                    document.getElementById('checkbox9').src=document.getElementById('checkbox9').src.replace('checked','checkbox')
            }
            element.src=element.src.replace('checkbox', 'checked')
            if (element.id=='checkbox6')
                walkProblem="רק בתוך הדירה"
            if (element.id=='checkbox7')
                walkProblem="בסביבה הקרובה"
            if (element.id=='checkbox8')
                walkProblem="יכול/ה ללכת מעל 20 דקות רצוף"
            if (element.id=='checkbox9')
                walkProblem="לא יכול/ה ללכת"
        }
        else
        {
           element.src=element.src.replace('checked', 'checkbox')
           walkProblem=""
        }
        toggleNextButton()
    }

    var handsProblem=""

    function markCheckbox3(element) {
        if (element.src.endsWith('checkbox.png'))
        {
            if (handsProblem!="")
            {
                if (handsProblem=='משתמש/ת בשתי הידיים בהצלחה')
                    document.getElementById('checkbox10').src=document.getElementById('checkbox10').src.replace('checked','checkbox')
                if (handsProblem=='משתמש/ת ביד אחת')
                    document.getElementById('checkbox11').src=document.getElementById('checkbox11').src.replace('checked','checkbox')
                if (handsProblem=='לא משתמש/ת בידיים')
                    document.getElementById('checkbox12').src=document.getElementById('checkbox12').src.replace('checked','checkbox')
            }
            element.src=element.src.replace('checkbox', 'checked')

            if (element.id=='checkbox10')
                handsProblem="משתמש/ת בשתי הידיים בהצלחה"
            if (element.id=='checkbox11')
                handsProblem="משתמש/ת ביד אחת"
            if (element.id=='checkbox12')
                handsProblem="לא משתמש/ת בידיים"
        }
        else
        {
           element.src=element.src.replace('checked', 'checkbox')
           handsProblem=""
        }
        toggleNextButton()
    }


    function chooseYesOrNo(element)
    {
        if ((document.getElementById("yesButton").src.endsWith('yesButton.png'))||(document.getElementById("noButton").src.endsWith('noButton.png')))
        {
            if (selectedYesOrNo!="")
            {
                if (selectedYesOrNo=="yes")
                    document.getElementById('yesButton').src=document.getElementById('yesButton').src.replace('yesButtonPurple','yesButton')
                if (selectedYesOrNo=="no")
                    document.getElementById('noButton').src=document.getElementById('noButton').src.replace('noButtonPurple','noButton')
            }
            if (element.id=='yesButton')
            {
                document.getElementById('yesButton').src=document.getElementById('yesButton').src.replace('yesButton','yesButtonPurple')
                selectedYesOrNo="yes"
            }
            if (element.id=='noButton')
            {
                document.getElementById('noButton').src=document.getElementById('noButton').src.replace('noButton','noButtonPurple')
                selectedYesOrNo="no"
            }
        }
        else
           selectedYesOrNo=""
        toggleNextButton()
    }

    function chooseYes()
    {
        if (document.getElementById("yesButton").src.endsWith('yesButton.png'))
        {
                document.getElementById("yesButton").src=document.getElementById("yesButton").src.replace('yesButton', 'yesButtonPurple')
                document.getElementById("noButton").src=document.getElementById("noButton").src.replace('noButton', 'noButton')
        }
        selectedYesOrNo="yes"
        toggleNextButton()
    }

    function chooseNo()
    {
        if (document.getElementById("noButton").src.endsWith('noButton.png'))
        {
                document.getElementById("yesButton").src=document.getElementById("yesButton").src.replace('yesButton', 'yesButton')
                document.getElementById("noButton").src=document.getElementById("noButton").src.replace('noButton', 'noButtonPurple')

        }
        selectedYesOrNo="no"
        toggleNextButton()
    }

    function canClickNext()
    {
        if ((epilepsy=="" && downSyndrom=="" && muscleDystrophy=="" && heartProblem=="" && noProblem=="") || (walkProblem=="") || (handsProblem=="") || (selectedYesOrNo==""))
            return false
        else
            return true
    }

    function toggleNextButton()
    {
        if(canClickNext())
            document.getElementById("button").style.opacity="1"
        else
            document.getElementById("button").style.opacity="0.2"
    }

    function nextScreen()
        {
            selectNum=document.getElementById('num').value;
            console.log(epilepsy, downSyndrom, muscleDystrophy, heartProblem, noProblem, walkProblem, handsProblem, selectedYesOrNo)
            if (!canClickNext())
                alert("ענה על כל הסעיפים")
            else
                window.location.href="/selectHealth?epilepsy="+epilepsy+"&downSyndrom="+downSyndrom+"&muscleDystrophy="+muscleDystrophy+"&heartProblem="+heartProblem+"&noProblem="+noProblem+"&walkProblem="+walkProblem+"&handsProblem="+handsProblem+"&selectedYesOrNo="+selectedYesOrNo+"&selectNum="+selectNum

        }
