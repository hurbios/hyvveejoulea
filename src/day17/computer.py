class Computer:
    def __init__(self, a, b, c, program):
        self._register_a = a
        self._register_b = b
        self._register_c = c
        self._instruction_pointer = 0
        self._program = program
        self._printout = ""

    def _get_combo_operand_value(self, operand):
        if operand < 4 and operand >= 0:
            return operand
        match operand:
            case 4:
                return self._register_a
            case 5:
                return self._register_b
            case 6:
                return self._register_c

    def adv(self, combo_operand):
        operand = self._get_combo_operand_value(combo_operand)
        denominator = 2**operand
        self._register_a //= denominator
        self._instruction_pointer += 2
        # self._register_a = self._register_a >> denominator


    def bxl(self, operand):
        self._register_b = self._register_b ^ operand
        self._instruction_pointer += 2


    def bst(self, combo_operand):
        self._register_b = self._get_combo_operand_value(combo_operand) % 8
        self._instruction_pointer += 2

    def jnz(self, operand):
        if self._register_a != 0:
            self._instruction_pointer = operand
        else:
            self._instruction_pointer += 2


    def bxc(self, _):
        self._register_b = self._register_b^self._register_c
        self._instruction_pointer += 2

    def out(self, combo_operand):
        operand = self._get_combo_operand_value(combo_operand)
        self._instruction_pointer += 2
        opmod8 = operand % 8
        self._printout += str(opmod8) if len(self._printout) == 0 else "," + str(opmod8)
        # return operand % 8        

    def bdv(self,combo_operand):
        operand = self._get_combo_operand_value(combo_operand)
        denominator = 2**operand
        self._register_b = self._register_a // denominator
        self._instruction_pointer += 2


    def cdv(self,combo_operand):
        operand = self._get_combo_operand_value(combo_operand)
        denominator = 2**operand
        self._register_c = self._register_a // denominator
        self._instruction_pointer += 2

    def execute_function(self, opcode, operand):
        match opcode:
            case 0:
                return self.adv(operand)
            case 1:
                return self.bxl(operand)
            case 2:
                return self.bst(operand)
            case 3:
                return self.jnz(operand)
            case 4:
                return self.bxc(operand)
            case 5:
                return self.out(operand)
            case 6:
                return self.bdv(operand)
            case 7:
                return self.cdv(operand)

    def start_program(self):
        while len(self._program) > self._instruction_pointer:
            self.execute_function(self._program[self._instruction_pointer], self._program[self._instruction_pointer+1])
        # print(self._printout)

    def get_register_a(self):
        return self._register_a
    def get_register_b(self):
        return self._register_b
    def get_register_c(self):
        return self._register_c
    
    def get_printout(self):
        return self._printout
    

