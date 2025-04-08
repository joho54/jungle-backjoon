import sys

def parse(string: str):
    numeric_tmp = ''
    listed = []
    for s in string:
        if s.isnumeric():
            numeric_tmp += s
        else:
            listed.append(int(numeric_tmp))
            listed.append(s)
            numeric_tmp = ''
    
    listed.append(int(numeric_tmp))
    return listed

def greedy(listed: list):
    neg_flag = False
    result = 0
    for l in listed:
        if isinstance(l, int):
            if neg_flag:
                result -= l
            else:
                result += l
        else:
            if l == '-' and neg_flag != True:
                neg_flag = True
    return result

def solve(string):
    listed = parse(string)
    result = greedy(listed)
    return result

def test():
    string = '55-50+40'
    assert solve(string) == -35
    string = '10+20+30+40' 
    assert solve(string) == 100
    string = '00009-00009'
    assert solve(string) == 0
    string = '1231-1231-1231'
    assert solve(string) == -1231


if __name__ == '__main__':	
    input = sys.stdin.readline
    string = input().strip()
    print(solve(string))
    # test()
    