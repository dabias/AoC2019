for noun in range(100):
    for verb in range(100):
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]
        pc =0
        program[1] = noun
        program[2] = verb
        while True:
            if (program[pc] == 1):
                program[program[pc+3]] = program[program[pc+1]]+program[program[pc+2]]
            elif program[pc] == 2:
                program[program[pc+3]] = program[program[pc+1]]*program[program[pc+2]]
            elif program[pc] == 99:
                if (program[0] == 19690720):
                    print(noun,verb)
                break
            else:
                print('unexpected or absent opcode')
                break

            pc = pc+4

        
