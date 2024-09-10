from collections import defaultdict
def solution(properWords, mistypes):
    hm = dict()
    for word in properWords:
        for i in range(len(word)):
           prefix = word[:i]
           suffix = word[i + 1:] 
           wildcard = prefix + "*" + suffix
           hm[wildcard] = word
    res = []
    for mistype in mistypes:
        for i in range(len(mistype)):
            prefix = mistype[:i]
            suffix = mistype[i + 1:] 
            wildcard = prefix + "*" + suffix
            if wildcard in hm.keys():
                res.append(hm[wildcard])
    return res