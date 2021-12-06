class Physician:
    __slots__ = ['__id', '__name', '__specialty']
    def __init__(self, id, name, specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty
    def __repr__(self):
        return self.__id+','+ self.__name+','+ self.__specialty
    def __str__(self):
        return self.__id+','+ self.__name+','+ self.__specialty

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_specialty(self):
        return self.__specialty

    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_specialty(self, specialty):
        self.__specialty = specialty

class Patient:
    __slots__ = ['__emr_id', '__name', '__gender', '__p_number']
    def __init__(self, emr_id, name, gender, p_number):
        self.__emr_id = emr_id
        self.__name = name
        self.__gender = gender
        self.__p_number = p_number
    def __repr__(self) -> str:
        return self.__emr_id+','+ self.__name+','+ self.__gender+','+ self.__p_number
    
    def get_emr_id(self):
        return self.__emr_id
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_p_number(self):
        return self.__p_number

    def set_emr_id(self, emr_id):
        self.__emr_id = emr_id
    def set_name(self, name):
        self.__name = name
    def set_gender(self, gender):
        self.__gender = gender
    def set_p_number(self, p_number):
        self.__p_number = p_number
    
class Encounter:
    __slots__ = ['Physician', 'Patient', 'date', 'disease', 'medication']
    def __init__(self, Physician, Patient, date, disease, medication):
        self.Physician = Physician
        self.Patient = Patient
        self.date = date
        self.disease = disease
        self.medication = medication
    
    def __str__(self):
        return str(self.Physician)+','+str(self.Patient)+','+self.date+','+self.disease+','+self.medication

def patientReader():
    with open ("patients.csv", 'r') as x:
        P = []
        for i in x:
            l = i[:-1].split(',')
            P += [l]

    p0 = Patient(P[0][0], P[0][1], P[0][2], P[0][3])
    p1 = Patient(P[1][0], P[1][1], P[1][2], P[1][3])
    p2 = Patient(P[2][0], P[2][1], P[2][2], P[2][3])
    p3 = Patient(P[3][0], P[3][1], P[3][2], P[3][3])
    p4 = Patient(P[4][0], P[4][1], P[4][2], P[4][3])
    p5 = Patient(P[5][0], P[5][1], P[5][2], P[5][3])
    p6 = Patient(P[6][0], P[6][1], P[6][2], P[6][3])
    p7 = Patient(P[7][0], P[7][1], P[7][2], P[7][3])
    p8 = Patient(P[8][0], P[8][1], P[8][2], P[8][3])
    p9 = Patient(P[9][0], P[9][1], P[9][2], P[9][3])

    return [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]


def physicianReader():
    with open ("physicians.csv", 'r') as x:
        P = []
        for i in x:
            l = i[:-1].split(',')
            P += [l]
    p0 = Physician(P[0][0], P[0][1], P[0][2])
    p1 = Physician(P[1][0], P[1][1], P[1][2])
    p2 = Physician(P[2][0], P[2][1], P[2][2])

    return [p0, p1, p2]

def encounterSave(E):
    import csv
    with open('encounter.csv', 'w') as x:
        for i in E:
            x.write(str(i)+'\n')

def main():
    P1 = patientReader()
    P2 = physicianReader()
    e1 = Encounter(P2[2], P1[0], '12Nov', 'anemia', 'Iron')
    e2 = Encounter(P2[0], P1[4], '13Nov', 'leukamia', 'Transfusion')
    e3 = Encounter(P2[1], P1[3], '14Nov', 'Cavities', 'Calcium')
    e4 = Encounter(P2[0], P1[6], '15Nov', 'cancer', 'Surgery')
    e5 = Encounter(P2[2], P1[2], '16Nov', 'tummy pain', 'antacid')
    E = [e1, e2, e3, e4, e5]

    for i in P1:
        print(i)
    print()
    for i in P2:
        print(i)
    print()
    for i in E:
        print(i)
    encounterSave(E)

main()