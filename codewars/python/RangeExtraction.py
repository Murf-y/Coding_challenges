def solution(args):
    run = []
    res = []
    first, *rest = args
    run.append(first)

    for n in rest+['end marker']:
        if n != run[-1] + 1:
            if len(run) > 2:
                res.append(f'{run[0]}-{run[-1]}')
            else:
                res += [str(r) for r in run]    #either one number, or two consecutive numbers
            run = [n]
        else:
            run.append(n)

    return ','.join(res)
