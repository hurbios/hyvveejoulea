from computer import Computer
import z3

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
    # a,b,c,program = readFile("./test_input2.txt")
    # a,b,c,program = readFile("./test_input.txt")
    a,b,c,program = readFile("./input.txt")
    

    print("program", program)
    computer=Computer(a,b,c,program)
    computer.start_program()
    print(computer.get_printout())

    fail = 0

    expected_printout = ",".join(map(lambda x: str(x),program))
    # for i in range(35184372000000,35185000000100):
    # for i in range(265400378784736,266474976500000,1):
    # for i in range(265400377933816,266474976500000,100):
    #     computer=Computer(i,b,c,program)
    #     computer.start_program()
    #     pritt = computer.get_printout()
    #     # print(i, "-", pritt, len(pritt))
    #     # if pritt == expected_printout:
    #     # if not pritt.endswith("7,0,3,4,1,5,5,3,0"):
    #     #     fail +=1
    #     #     if fail > 1:
    #     #         print(i, "too high")
    #     #         break
    #     if pritt.endswith("1,7,0,3,4,1,5,5,3,0"):
    #         print(i, "-", pritt, len(pritt))
    #         print("register a for copy: ", i)
    #         # break


    # print("program", program)
    # computer=Computer(a,b,c,program)
    # computer.start_program()
    # print("registers a,b,c: ",computer.get_register_a(),computer.get_register_b(),computer.get_register_c())

    bv = z3.BitVec('bv', 64)
    a = bv
    b = 0
    c = 0
    s = z3.Optimize()

    print(program)
    for x in program:
        b = a % 8
        b = b ^ 7
        c = a / (1 << b)
        b = b ^ 7
        a /= 1 << 3
        b = b ^ c
        s.add(b % 8 == x)
    s.add(a == 0)
    s.minimize(bv)
    # print(s.objectives())
    print(s.check())
    print(s.model().eval(bv))

    # start
    #     bst(4) => b = a % 8
    #     bxl(7) => b = b ^ 7 (0111)
    #     cdv(5) => c = a // 2**b
    #     bxl(7) => b = b ^ 7 (0111)
    #     adv(3) => a = a // 2**3
    #     bxc(_) => b = b ^ c
    #     out(5) => print b % 8
    #     jnz(0) => jump 0 if a != 0

if __name__ == "__main__":
    run()
