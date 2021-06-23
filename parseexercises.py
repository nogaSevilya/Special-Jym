import pandas as pd
import random
import pyttsx3
import time


from exercise import exercise
from user import user

#הפונקציה הופכת את הטבלה של התרגילים למערך של אובייקטי תרגילים.
def getAllExercises (exerFile):
    exercises = []
    for index, row in exerFile.iterrows():
        exer = exercise(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12], row[13], row[14], row[15], row[16])
        exercises.append(exer)
    return exercises

#הפונקציה מסננת מכלל התרגילים רק את התרגילים שהספורטאי יכול לעשות.
def filterExercises(allExercises, userCapabilities):
    allowedExercises = []
    for e in allExercises:
        if e.canDoExercise(userCapabilities):
            allowedExercises.append(e)
    return allowedExercises

#הפונקציה הופכת את טבלת נתוני הספורטאים למערך של אובייקטי ספורטאים.
def getAllUsers(userFile):
    users = []
    for index, row in userFile.iterrows():
        users.append(user(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                        row[11], row[12]))
    return users

#בניית חימום ושחרור:
#הפונקציה מסננת מכל התרגילים שהספורטאי יכול לעשות רק את תרגילי החימום, ושומרת אותם ברשימה.
def filterWarmup(allExercises):
    warmupExercises = []
    for e in allExercises:
        if e.warmup:
            warmupExercises.append(e)
    return warmupExercises

#הפונקציה בונה רצף רנדומלי של תרגילי חימום ושחרור ומוסיפה אותם לרשימה.
def buildWarmupCooldown(setNum, exerciseNum, allowedExercises):
    exercises = filterWarmup(allowedExercises)
    warmup = []
    random.shuffle(exercises)
    for i in range(setNum):
        for j in range(exerciseNum):
            warmup.append(exercises[j])
    return warmup

#בניית תרגילי האימון עצמו:
#הפונקציה מסננת מכל התרגילים שהספורטאי יכול לעשות רק את תרגילי האימון עצמו, ושומרת אותם ברשימה.
def filterWorkout(allExercises, type, muscle):
    workoutExercises = []
    for e in allExercises:
        if e.muscle == 'Full Body' or muscle == e.muscle:
            if e.type.find(type) != -1:
                workoutExercises.append(e)
    return workoutExercises

#הפונקציה בונה סט תרגילים ומכניסה אותם למערך.
def buildSet(setNum, exerciseNum, allowedExercises, exerType, muscle):
    exercises = filterWorkout(allowedExercises, exerType, muscle)
    if len(exercises) < exerciseNum:
        exercises = allowedExercises
    result = []
    random.shuffle(exercises)
    for i in range(setNum):
        for j in range(exerciseNum):
            result.append(exercises[j])
    return result

#שילוב שמע:
engine = pyttsx3.init()

def talk(text):
    print(text)
    #engine.say(text)
    #engine.save_to_file(text, 'speech.mp3')
    #engine.runAndWait()

#הפונקציה מדפיסה ומשמיעה את שם התרגיל ומודיעה כשיש הפסקה בין תרגילים.
def doExercise(exercise):
    print(exercise.name)
    #talk(exercise.name)
    #time.sleep(30)
    #talk('break')
    #time.sleep(10)

exercises = getAllExercises(pd.read_excel ('C:/Users/NOGA/Downloads/נתוני התרגילים שיש לאסוף .xlsx'))
users = getAllUsers(pd.read_excel('C:/Users/NOGA/Downloads/שאלון לספורטאי ספיישל אולימפיקס (תגובות).xlsx'))

def buildRatingFile():
    #הפונקציה מכניסה ציון, שם משתמש וקוד אימון לטבלת הדירוגים
    df=pd.DataFrame()
    listRating=[]
    listUsername=[]
    workouts = pd.read_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx')
    for user in users:
        listRating.append(random.randint(1, 3))
        listUsername.append(user.name)
    df['rating'] = listRating
    df['username'] = listUsername
    df['workoutId'] = workouts['workoutId'].values
    df.to_excel('C:/Users/NOGA/Documents/טבלת דירוגים.xlsx', 'Sheet1')


def makeWorkout():
    #הדפסת והשמעת שישה סטים של תרגילים מהסוגים השונים ומפלג גוף עליון ופלג גוף תחתון, כולל חימום ושחרור.
    #בנוסף, הפונקציה מכניסה רשימת תרגילים של כל אימון לקובץ האקסל של "טבלת אימונים" לצורך שמירתם.
    workoutId=99
    listworkouts = []
    listId = []
    df = pd.DataFrame()
    for user in users:
        print(user.name)
        # הדפסת תרגילים שהמשתמש יכול לעשות
        workout=buildExercise(user, exercises)
        workoutId+=1
        listId.append(workoutId)
        listworkouts.append(workout)
    df['workoutId'] = listId
    df['exercise'] = listworkouts
    df.to_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx', 'Sheet2')


def buildExercise(user, exercises):
    allowedExercises = filterExercises(exercises, user)
    warmup = buildWarmupCooldown(3, 3, allowedExercises)
    exerciseList = {}
    talk('warmup:')
    print('warmup')
    warmupList=[]
    for i in warmup:
        doExercise(i)
        warmupList.append(i.name)
    exerciseList['warmup']=warmupList
    print('Set 1')
    talk('Set 1')
    set1=[]
    for i in buildSet(2, 4, allowedExercises, 'cardio', 'lower body'):
        doExercise(i)
        set1.append(i.name)
    exerciseList['set 1']=set1

    set2 = []
    print('Set 2')
    talk('Set 2')
    for i in buildSet(2, 4, allowedExercises, 'cardio', 'upper body'):
        doExercise(i)
        set2.append(i.name)
    exerciseList['set 2'] = set2

    set3 = []
    print('Set 3')
    talk('Set 3')
    for i in buildSet(2, 3, allowedExercises, 'flexibility', 'lower body'):
        doExercise(i)
        set3.append(i.name)
    exerciseList['set 3'] = set3

    set4 = []
    print('Set 4')
    talk('Set 4')
    for i in buildSet(2, 3, allowedExercises, 'flexibility', 'upper body'):
        doExercise(i)
        set4.append(i.name)
    exerciseList['set 4'] = set4

    set5= []
    print('Set 5')
    talk('Set 5')
    for i in buildSet(2, 3, allowedExercises, 'strength', 'lower body'):
        doExercise(i)
        set5.append(i.name)
    exerciseList['set 5'] = set5

    set6 = []
    print('Set 6')
    talk('Set 6')
    for i in buildSet(2, 3, allowedExercises, 'strength', 'upper body'):
        doExercise(i)
        set6.append(i.name)
    exerciseList['set 6'] = set6

    talk('well done')
    exerciseList['cooldown']=warmupList
    return exerciseList

#מודל המלצות:
#הפונקציה מוצאת משתמשים דומים. היא בודקת אם הם עשו אימון ודירגו אותו גבוה. אם כן- היא ממליצה את האימון שהם עשו למשתמש הנוכחי.
def recommendWorkout(user):
    rating=pd.read_excel('C:/Users/NOGA/Documents/טבלת דירוגים.xlsx')
    workouts=pd.read_excel('C:/Users/NOGA/Documents/טבלת אימונים.xlsx')
    for i in users:
        index=users.index(i)
        if((user.isEqual(i))and(int(rating.iloc[index][1])>2)):
            for index, workout in workouts.iterrows():
                if(rating.iloc[index][3]==workout['workoutId']):
                    return (workout['exercise'])
    return (buildExercise(user, exercises))
#הפעלת הפונקציה שבונה אימון


def main():

    makeWorkout()
    buildRatingFile()
    print(recommendWorkout(user('name', 'גבר', 180, 180, 2,
                 'רק בתוך הדירה', 'פעמיים או יותר',  'לא משתמש/ת בידיים', 'יש והיה התקף בשנים האחרונות',
                 'יש', 'אין', 'אין', 'גב')))

    print(recommendWorkout(user('אור מוס', 'אישה', 60, 163, 3,
                 'יכול/ה ללכת מעל 20 דקות רצוף', 'לא',  'משתמש/ת בשתי הידיים בהצלחה', 'אין',
                 'אין', 'אין', 'אין', 'אין')))

if __name__ == "__main__":
    main()