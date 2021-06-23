class user:
    def parseNumPerWeek(self, numPerWeek):
        if numPerWeek == 'לא מתאמן בכלל':
            return 0
        if numPerWeek == 'פעם בשבוע':
            return 1
        if numPerWeek == 'פעמיים בשבוע':
            return 2
        else:
            return 3

    def __init__(self, name, gender, weight, height, numPerWeek,
                 aerobicAndWalkProblem, fallRisk, handCordinationProblem, epilepsy,
                 downSyndrom, muscleDystrophy, heartProblem, chronicCondition):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.height = height
        self.numPerWeek = self.parseNumPerWeek(numPerWeek)
        self.aerobicAndWalkProblem = (aerobicAndWalkProblem == 'רק בתוך הדירה' or aerobicAndWalkProblem == 'לא יכול/ה ללכת')
        self.fallRisk = (fallRisk == 'פעמיים או יותר')
        self.balanceProblem = self.fallRisk
        self.handCordinationProblem = (handCordinationProblem == 'לא משתמש/ת בידיים')
        self.epilepsy = (epilepsy == 'יש והיה התקף בשנים האחרונות')
        self.downSyndrom = (downSyndrom == 'יש')
        self.muscleDystrophy = (muscleDystrophy == 'יש')
        self.heartProblem = (heartProblem == 'יש')
        self.chronicCondition = chronicCondition
        self.neck = (chronicCondition.find('צוואר') != -1)
        self.shoulders = (chronicCondition.find('כתף') != -1)
        self.back = (chronicCondition.find('גב') != -1)
        self.leg = (chronicCondition.find('רגל') != -1)

    def isEqual(self, user):
        if ((self.aerobicAndWalkProblem==user.aerobicAndWalkProblem)and(self.fallRisk==user.fallRisk)and(self.balanceProblem==user.balanceProblem)and(self.handCordinationProblem==user.handCordinationProblem)and(self.downSyndrom==user.downSyndrom)and(self.muscleDystrophy==user.muscleDystrophy)and(self.heartProblem==user.heartProblem)and(self.chronicCondition==user.chronicCondition)):
            return True

        else:
            return False



