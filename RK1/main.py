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

class ProgramsOfComputer:
    def __init__(self, com, prog):
        self.com = com
        self.prog = prog
 
computers = [
    Computer(1, 'Aero Computer', 'Lenovo'),
    Computer(2, 'Sigma Computer', 'Acer'),
    Computer(3, 'Alfa Computer', 'Mac'),
]

programs = [
    Program(1, 'Task Manager', 'v1.0', 1),
    Program(2, 'Photoshop', 'v2.1', 2),
    Program(3, 'Media Player', 'v3.5', 3),
    Program(4, 'Steam', 'v1.2', 1),
    Program(5, 'Minecraft', 'v4.0', 2)
]

programs_of_computers = [
    ProgramsOfComputer(computers[0], programs[0]),
    ProgramsOfComputer(computers[1], programs[1]),
    ProgramsOfComputer(computers[2], programs[2]),
    ProgramsOfComputer(computers[0], programs[3]),
    ProgramsOfComputer(computers[1], programs[4])
]

def main():
    one_to_many = [(program.program_name, program.version, com.computer_name)
                   for com in computers
                   for program in programs
                   if program.computerId == com.id]

    many_to_many_temp = [(com.computer_name, cd.com.id, cd.prog.id)
                         for com in computers
                         for cd in programs_of_computers if com.id == cd.com.id]

    many_to_many = [(program.program_name, program.version, com_name)
                    for com_name, com_id, program_id in many_to_many_temp
                    for program in programs if program.id == program_id]
    
#1.1-М.Список компьютеров, у которых название начинается с буквы «A», и список установленных программ.
    temp_result1 = [computer for computer in computers if computer.computer_name.startswith('A')]
    result_1={}
    print("\n1:")
    for computer in temp_result1:
        result_1[computer.computer_name]=[program.program_name for program in programs if program.computerId==computer.id]

    print(result_1)

#2.1-М.Список компьютеров с максимальной версией программ, отсортированный по максимальной версии.
    result2 = [(com_name, max([float(version.split('v')[1]) for program_name, version, name in one_to_many if name == com_name]))
               for com_name in set([com_name for _, _, com_name in one_to_many])]
    result2 = sorted(result2, key=itemgetter(1), reverse=True)
    print("\n2:")
    for com_name, min_version_count in result2:
        print(f"компьютер:{com_name}, максимальная версия его программ:{min_version_count}")

#3.М-М.Список всех связанных компьютеровков и программ, отсортированный по компьютерам, сортировка по программам произвольная
    result3 = sorted(many_to_many, key=itemgetter(2))
    print("\n3:")
    for program_name, version, com_name in result3:
        print(f"компьютер:{com_name}, программа:{program_name}")

if __name__ == '__main__':
    main()