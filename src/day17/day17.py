from computer import Computer

def readFile(file_path):
    a = 0
    b = 0
    c = 0
    program = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            if "Register A: " in row:
                a = int(row.replace("\n", "").replace("Register A: ", ""))
            elif "Register B: " in row:
                b = int(row.replace("\n", "").replace("Register B: ", ""))
            elif "Register C: " in row:
                c = int(row.replace("\n", "").replace("Register C: ", ""))
            elif "Program: " in row:
                for num in row.replace("\n", "").replace("Program: ", "").split(","):
                    program.append(int(num))
    return a,b,c,program


def run():
    # a,b,c,program = readFile("./test_input.txt")
    a,b,c,program = readFile("./input.txt")
    

    print("program", program)
    computer=Computer(a,b,c,program)
    computer.start_program()


    # print("program", program)
    # computer=Computer(a,b,c,program)
    # computer.start_program()
    # print("registers a,b,c: ",computer.get_register_a(),computer.get_register_b(),computer.get_register_c())

if __name__ == "__main__":
    run()
