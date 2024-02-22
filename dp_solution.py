import pprint


class Subject:
    def __init__(self, name, time, main):
        self.name = name
        self.time = time
        self.main = main

    def __str__(self):
        return f'{self.name}, {self.time}, {self.main}'

    def __repr__(self):
        return f'{self.name}, {self.time}, {self.main}'


def fnc(subjects_arr):
    subjects_length = len(subjects_arr)
    answer = [[[subjects_arr[0]]] * subjects_length]

    for current_subject_number in range(0, subjects_length):
        previous_row = answer[current_subject_number]
        current_subject = subjects_arr[current_subject_number]
        current_subject_time = current_subject.time
        current_subject_main = current_subject.main
        new_row = [[]] * subjects_length

        for i in range(1, subjects_length + 1):
            previous_subjects = previous_row[i - 1].copy()
            previous_subjects_main = 0
            for s in previous_subjects:
                previous_subjects_main += s.main
            cell_time = i * 0.5

            if current_subject_time <= cell_time:

                if cell_time == current_subject_time:
                    if current_subject_main >= previous_subjects_main:
                        new_row[i - 1].append(current_subject)
                    else:
                        new_row[i - 1] = previous_subjects

                if cell_time > current_subject_time:
                    difference = cell_time - current_subject_time
                    added_subjects = previous_row[int(difference / 0.5) - 1].copy()
                    if current_subject not in added_subjects:
                        added_subjects.append(current_subject)

                    added_subjects_main = 0

                    for added_subject in added_subjects:
                        added_subjects_main += added_subject.main

                    if added_subjects_main >= previous_subjects_main:
                        if current_subject not in added_subjects:
                            added_subjects.append(current_subject)
                        new_row[i - 1] = added_subjects
                    else:
                        new_row[i - 1] = previous_subjects

            else:
                new_row[i - 1] = previous_subjects
        answer.append(new_row)

    return answer


inp = [Subject('Математика', 1, 9),
       Subject('Биология', 0.5, 5),
       Subject('Русский', 1, 6),
       Subject('Информатика', 0.5, 7),
       Subject('Китайский', 1.5, 9),
       Subject('Физика', 2, 10)]

inp = sorted(inp, key=lambda x: x.time)

answer = fnc(inp)
pprint.pprint(answer)
