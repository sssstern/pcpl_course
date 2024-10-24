from operator import itemgetter

class Program:
    def __init__(self, program_id, name, version, computerId):
        self.id = program_id
        self.program_name = name
        self.version = version
        self.computerId = computerId

class Computer:
    def __init__(self, computer_id, name, developer):
        self.id = computer_id
        self.computer_name = name
        self.developer=developer

"""class ProgramsOfComputer:
   def __init__(self, program_id, computer_id):
        self.program_id = program_id
        self.computer_id = computer_id
"""
class ProgramsOfComputer:
    def __init__(self, doc, part):
        self.doc = doc
        self.part = part
 
computers = [
    Computer(1, 'Alpha Computer', 'Lenovo'),
    Computer(2, 'Beta Computer', 'Acer'),
    Computer(3, 'Aqua Computer', 'Mac')
]

programs = [
    Program(1, 'Text Editor', 'v1.0', 1),
    Program(2, 'Browser', 'v2.1', 2),
    Program(3, 'Media Player', 'v3.5', 3),
    Program(4, 'Image Editor', 'v1.2', 1),
    Program(5, 'Tideo Editor', 'v4.0', 2)
]

programs_of_computers = [
    ProgramsOfComputer(computers[0], programs[0]),
    ProgramsOfComputer(computers[1], programs[1]),
    ProgramsOfComputer(computers[2], programs[2]),
    ProgramsOfComputer(computers[0], programs[3]),
    ProgramsOfComputer(computers[1], programs[4])
]

def main():
    one_to_many = [(program.program_name, program.version, doc.computer_name)
                   for doc in computers
                   for program in programs
                   if program.computerId == doc.id]

    many_to_many_temp = [(doc.computer_name, cd.doc.id, cd.part.id)
                         for doc in computers
                         for cd in programs_of_computers if doc.id == cd.doc.id]

    many_to_many = [(program.program_name, program.version, doc_name)
                    for doc_name, doc_id, program_id in many_to_many_temp
                    for program in programs if program.id == program_id]
    
#1.1-М.Список компьютеров, у которых название начинается с буквы «Т», и список установленных программ.
    temp_result1 = [computer for computer in computers if computer.computer_name.startswith('A')]
    result_1={}
    for computer in temp_result1:
        result_1[computer.computer_name]=[program.program_name for program in programs if program.computerId==computer.id]

    print(result_1)

#2.1-М.Список компьютеров с максимальной версией программ, отсортированный по максимальной версии.
    result2 = [(doc_name, max([float(version.split('v')[1]) for chapter_name, version, name in one_to_many if name == doc_name]))
               for doc_name in set([doc_name for _, _, doc_name in one_to_many])]
    result2 = sorted(result2, key=itemgetter(1), reverse=True)
    print("\n2:")
    for doc_name, min_version_count in result2:
        print(f"компьютер:{doc_name}, максимальная версия его программ:{min_version_count}")

#3.М-М.Список всех связанных компьютеровков и программ, отсортированный по компьютерам, сортировка по программам произвольная
    result3 = sorted(many_to_many, key=itemgetter(2))
    print("\n3:")
    for program_name, version, doc_name in result3:
        print(f"компьютер:{doc_name}, программа:{program_name}")

if __name__ == '__main__':
    main()