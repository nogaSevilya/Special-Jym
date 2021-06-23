from flask import Flask , send_from_directory, request, session, render_template, flash, url_for, redirect
from werkzeug.utils import redirect
from user import user
from parseexercises import getAllExercises, getAllUsers, buildExercise
import pandas as pd
import pyttsx3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hvre6bhsj4df'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/html/<path:path>')
def send_html(path):
    return send_from_directory('html', path)

@app.route('/selectName', methods=['GET', 'POST'])
def selectName():
    session['name']=request.args.get('name')
    users = getAllUsers(pd.read_excel('C:/Users/NOGA/Downloads/שאלון לספורטאי ספיישל אולימפיקס (תגובות).xlsx'))
    for i in users:
        if(session['name']==i.name):
            return redirect("html/questionnaire-painFront.html")
    return redirect("html/instruction.html")

@app.route('/selectSex')
def selectSex():
    session['sex']=request.args.get('sex')
    return redirect("html/questionnaire-workoutsPerWeek.html")

@app.route('/selectWorkoutsPerWeek')
def selectWorkoutsPerWeek():
    session['workoutsPerWeek']=request.args.get('workoutsPerWeek')
    return redirect("html/questionnaire-health.html")

@app.route('/selectHealth')
def selectHealth():
    session['epilepsy']=request.args.get('epilepsy')
    session['downSyndrom']=request.args.get('downSyndrom')
    session['muscleDystrophy']=request.args.get('muscleDystrophy')
    session['heartProblem']=request.args.get('heartProblem')
    session['noProblem']=request.args.get('noProblem')

    if(session['noProblem']=="noProblem"):
        session['epilepsy']="אין"
        session['downSyndrom'] = "אין"
        session['muscleDystrophy'] = "אין"
        session['heartProblem'] = "אין"

    session['walkProblem'] = request.args.get('walkProblem')

    session['handsProblem']= request.args.get('handsProblem')

    session['selectedYesOrNo']= request.args.get('selectedYesOrNo')
    session['selectNum'] = request.args.get('selectNum')

    return redirect("html/prize.html")

@app.route('/selectHeight')
def selectHeight():
    session['height']=request.args.get('height')
    return redirect("html/questionnaire-weight.html")

@app.route('/selectWeight')
def selectWeight():
    session['weight']=request.args.get('weight')
    return redirect("html/prize2.html")

@app.route('/selectPain')
def selectPain():
    session['rightLeg']=request.args.get('rightLeg')
    session['leftLeg'] = request.args.get('leftLeg')
    session['rightHand'] = request.args.get('rightHand')
    session['leftHand'] = request.args.get('leftHand')
    session['neck'] = request.args.get('neck')
    session['abs'] = request.args.get('abs')
    session['back'] = request.args.get('back')
    return redirect("html/welcomeWorkout.html")

@app.route('/buildWorkout')
def buildWorkout():
    myUser=user(session['name'], session['sex'], session['weight'], session['height'], session['workoutsPerWeek'],
                session['walkProblem'], getFallRisk(), session['handsProblem'], session['epilepsy'],
                session['downSyndrom'], session['muscleDystrophy'], session['heartProblem'], getChronicCondition())
    exercises=getAllExercises(pd.read_excel ('C:/Users/NOGA/Downloads/נתוני התרגילים שיש לאסוף .xlsx'))
    workout=buildExercise(myUser, exercises)

    #שמירת אימון בדאטה סט
    dfWorkouts=pd.read_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx')
    newWorkout={}
    newWorkout['exercise'] = [workout]
    newWorkout['workoutId'] = len(dfWorkouts)+100
    session['workoutId'] = len(dfWorkouts)+100
    newWorkouts=dfWorkouts.append(pd.DataFrame(newWorkout), ignore_index=True)
    newWorkouts.to_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx')

    dfUsers=pd.read_excel('C:/Users/NOGA/Downloads/שאלון לספורטאי ספיישל אולימפיקס (תגובות).xlsx')

    #בדיקה האם המשתמש קיים בדאטה סט או לא (אם לא קיים בדאטה סט- צריך לשמור אותו)
    users = getAllUsers(pd.read_excel('C:/Users/NOGA/Downloads/שאלון לספורטאי ספיישל אולימפיקס (תגובות).xlsx'))
    for i in users:
        if (session['name'] == i.name):
            return render_template("workout.html", workout=workout)
    #שמירת משמש בדאטה סט
    newUser={}
    newUser['שם פרטי ומשפחה'] = session['name']
    newUser['מין'] = session['sex']
    newUser['משקל'] = session['weight']
    newUser['גובה'] = session['height']
    newUser['מספר אימונים בשבוע'] = session['workoutsPerWeek']
    newUser['יכולת אירובית גבוהה'] = session['walkProblem']
    newUser['נפילות'] = getFallRisk()
    newUser['רמת תפקוד ידיים'] = session['handsProblem']
    newUser['אפילפסיה'] = session['epilepsy']
    newUser['תסמונת דאון'] = session['downSyndrom']
    newUser['מחלה ניוונית'] = session['muscleDystrophy']
    newUser['בעיה לבבית'] = session['heartProblem']
    newUser['בעיות כרוניות'] = getChronicCondition()
    newUsers=dfUsers.append(pd.DataFrame(newUser, index=[0]), ignore_index=True)
    newUsers.to_excel('C:/Users/NOGA/Downloads/שאלון לספורטאי ספיישל אולימפיקס (תגובות).xlsx')

    return render_template("workout.html", workout=workout)

def getFallRisk():
    if(session['selectedYesOrNo']=='no'):
        return 'לא'
    if(session['selectNum']==1):
        return 'פעם אחת'
    return 'פעמיים ויותר'

def getChronicCondition():
    condition=[]
    if(session['rightLeg']=='רגל'):
        condition.append('רגל')
    if (session['leftLeg'] == 'רגל'):
        condition.append('רגל')
    if (session['rightHand'] == 'יד'):
        condition.append('יד')
    if (session['leftHand'] == 'יד'):
        condition.append('יד')
    if (session['neck'] == 'צוואר'):
        condition.append('צוואר')
    if (session['abs'] == 'בטן'):
        condition.append('בטן')
    if (session['back'] == 'גב'):
        condition.append('גב')
    if ((session['rightLeg'] == "") and (session['leftLeg'] == "") and (session['rightHand'] == "") and (session['leftHand'] == "") and (session['neck'] == "") and (session['abs'] == "") and (session['back'] == "")):
        return "אין"
    return ', '.join(condition)

@app.route('/selectRating')
def selectRating():
    session['rating']=request.args.get('rating')
    dfRating=pd.read_excel('C:/Users/NOGA/Documents/טבלת דירוגים.xlsx')
    dfWorkouts = pd.read_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx')

    #שמירת דירוג בדאטה סט
    newRating = {}
    newRating['rating'] = session['rating']
    newRating['username'] = session['name']
    newRating['workoutId'] = len(dfWorkouts) + 100
    session['workoutId'] = len(dfWorkouts) + 100
    newRatings = dfRating.append(pd.DataFrame(newRating, index=[0]), ignore_index=True)
    newRatings.to_excel('C:/Users/NOGA/Documents/טבלת דירוגים.xlsx')

    return redirect("/html/welcome.html")

if __name__ == '__main__':
    app.run(debug=True)