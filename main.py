

def f(s):
    di={}
    largest=0
    left=0
    for i in range(len(s)):
        check = di[s[i]]+1 if s[i] in di else 0
        left = max(left, check)
        largest=max(largest,i-left+1)
        di[s[i]]=i ## i + 1
    return largest

if __name__ == "__main__":
    print(f("ccabdec"))
