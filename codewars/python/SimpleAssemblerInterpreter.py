def simple_assembler(program):
    reg, i = {}, 0
    while i < len(program):
        cmd, k, v = (program[i] +' 0').split()[:3]
        if cmd == 'inc': reg[k] += 1
        if cmd == 'dec': reg[k] -= 1
        if cmd == 'mov': reg[k] = reg[v] if v in reg else int(v)
        if cmd == 'jnz' and (reg[k] if k in reg else int(k)):
            i += int(v) - 1
        i += 1
    return reg
