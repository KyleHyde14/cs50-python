import random

def main():
    level = get_level()
    problems = generate_problems(level)
    score = 0
    for p in range(len(problems)):
        tries = 3
        while tries > 0:
            try:
                ans = int(input(f'{problems[p][0]} = '))
            except ValueError:
                print('EEE')
                tries -= 1
                continue
            else:
                if ans == problems[p][1]:
                    score += 1
                    break
                else:
                    print('EEE')
                    tries -= 1
        if tries == 0:
            print(f'{problems[p][0]} = {problems[p][1]}')
            
    print(score)
    return''



def get_level():
    while True:
        try:
            level = int(input('Level: \n'))
            if not (0 < level < 4):
                continue
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if not (0 < level < 4):
        raise ValueError
    
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)   
    
    return random.randint(100, 999)

def generate_problems(level):
    problems = []

    for i in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        solution = X + Y
        problems.append((f'{X} + {Y}', solution))
    
    return problems
        



if __name__ == "__main__":
    print(main())
