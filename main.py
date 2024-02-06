#REMOVE PASS AND FIX THIS FUNCTION
def anagram(a,b):
    newA = ''.join(sorted(a))
    newB = ''.join(sorted(b))
    return newA == newB

if __name__ == '__main__':
    a = input()
    b = input()
    print(anagram(a,b))
    