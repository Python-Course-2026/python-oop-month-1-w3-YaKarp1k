class GradeBook:
    """ЗАДАЧА: Найти имя студента с самым высоким средним баллом"""
    def __init__(self): self.students = {} # {"Ivan": [5, 4], "Oleg": [3]}
    def get_best_student(self):
        if not self.students:
            return None

        mi = None
        best_name = None

        for name, score in self.students.items():
            avg = sum(score) / len(score)
            if mi is None or avg > mi:
                mi = avg
                best_name = name
        return best_name
