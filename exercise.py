class exercise:
    def __init__(self, name, equipment, level, type, muscle, description, neck, shoulders, back, leg, fallRisk,
                 walkProblem, handCordination, heartProblem, downSyndrom, muscleDystrophy, link):
        self.name = name
        self.equipment = equipment
        self.level = level
        self.type = type
        self.warmup = (type.find('warmup') != -1)
        self.cardio = (type.find('cardio') != -1)
        self.strength = (type.find('strength') != -1)
        self.flexibility = (type.find('flexibility') != -1)
        self.muscle = muscle
        self.description = description
        self.neck = (neck == 'yes')
        self.shoulders = (shoulders == 'yes')
        self.back = (back == 'yes')
        self.leg = (leg == 'yes')
        self.fallRisk = (fallRisk == 'yes')
        self.walkProblem = (walkProblem == 'yes')
        self.handCordination = (handCordination == 'yes')
        self.heartProblem = (heartProblem == 'yes')
        self.downSyndrom = (downSyndrom == 'yes')
        self.muscleDystrophy = (muscleDystrophy == 'yes')
        self.link = link

    def __str__(self):
        return '{} {} {}'.format(self.name, self.equipment, self.level)

    def canDoExercise(self, userCapabilities):
        if userCapabilities.muscleDystrophy and not self.muscleDystrophy:
            return False

        if userCapabilities.handCordinationProblem and not self.handCordination:
            return False

        if userCapabilities.neck and not self.neck:
            return False

        if userCapabilities.shoulders and not self.shoulders:
            return False

        if userCapabilities.back and not self.back:
            return False

        if userCapabilities.leg and not self.leg:
            return False

        if userCapabilities.heartProblem and not self.heartProblem:
            return False

        if userCapabilities.downSyndrom and not self.downSyndrom:
            return False

        if userCapabilities.aerobicAndWalkProblem and not self.walkProblem:
            return False

        if userCapabilities.balanceProblem and not self.fallRisk:
            return False

        else:
            return True

