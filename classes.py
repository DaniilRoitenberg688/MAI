class Room:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.subjectsAmount = 0

    def setAmountSubjects(self, count):
        self.subjectsAmount = count

    def getAmountSubjects(self) -> int:
        return self.subjectsAmount

    def setSubjects(self, subjects: list):
        self.subjects = subjects

    def getSubjects(self) -> list:
        return self.subjects

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def __iadd__(self, other: str):
        self.subjects.append(other)
        self.subjectsAmount += 1
        return self


