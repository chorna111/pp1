class U():
    id = 100000

    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = U.id
        U.id += 1

    def __str__(self):

        return f'{self.name} {self.surname}({self.id}),{self.field},UEK Kraków'


student = U('Anastasiia', 'Chorna', 'Applied informatics')

student2 = U('Jan', 'Kowalski', 'Finanse i rachunkowość')
student3 = U('Anna', 'Madej', 'Ekonomia')
print(student)
print(student2)
print(student3)
