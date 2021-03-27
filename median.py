import sys
testcase, num_of_values, total_questions = list(map(int,input().split()))
sys.stderr.write(str(testcase)+ str(num_of_values)+ str(total_questions)+'\n')

def find_min_and_max(candidate):
    while len(candidate) > 2: 
        first = candidate.pop()
        second = candidate.pop()
        third = candidate.pop()
        print(first, second, third)
        candidate.add(first)
        candidate.add(second)
        candidate.add(third)
        #print(first, second, third,file=sys.stderr)

        value = input()
        #print(int(value), file=sys.stderr)
        candidate.remove(int(value))
        #print(candidate, file=sys.stderr)
    return candidate

def solve_case(num_of_values):
    min_max_pairs = []
    candidate_original = set()
    for count in range(1,num_of_values+1):
        candidate_original.add(count)
    #print(candidate_original, file=sys.stderr)
    candidate = candidate_original.copy()

    for _ in range(int(num_of_values/2)):
        candiate_temp = candidate.copy()

        min_max = find_min_and_max(candiate_temp)
        min_max_pairs.append(tuple(min_max))
        #print(min_max, file=sys.stderr)

        for val in min_max:
            candidate.remove(val)
        #print(_, file=sys.stderr)
        #print(candidate, file=sys.stderr)
        #print(min_max_pairs, file=sys.stderr)

    answer = []
    index = 0
    for small, big in min_max_pairs:
        #print(answer, file=sys.stderr)
        #print(small, big, file=sys.stderr)
        answer.insert(index,small)
        answer.insert(len(answer)-index, big)
        index += 1

    #if int(value) == 1:
    #    pass
    #else:
    #iterate solution
    #print('answer: '+' '.join(str(item) for item in answer), file=sys.stderr)

    def switchero(solution, a_position):
        #print(solution, file=sys.stderr)
        b_position = len(solution)-a_position-1
        temp = solution[a_position]
        solution[a_position] = solution[b_position]
        solution[b_position] = temp
        #print(solution, file=sys.stderr)
        return solution

    for index in range(len(answer)-2):
        print(answer[index], answer[index+1], answer[index+2])
        #print(answer[index], answer[index+1], answer[index+2], file=sys.stderr)

        value = input()
        #print('res: '+value, file=sys.stderr)
        if int(value) == answer[index+1]:
            pass
        else:
            #print('unoh!!!', file=sys.stderr)
            answer = switchero(answer, index+1)

    #print(' '.join(str(item) for item in answer), file=sys.stderr)
    print(' '.join(str(item) for item in answer))
    value = input()
    print('judge says '+value, file=sys.stderr)

for i in range(int(testcase)):
    print('case '+str(i), file=sys.stderr)
    solve_case(num_of_values)


