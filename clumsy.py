from collections import defaultdict
from string import ascii_lowercase


def solution_adhy(properWords, mistypes):
    properWords = set(properWords)
    res = []
    for mistype in mistypes:
        for i in range(len(mistype)):
            prefix = mistype[:i]
            suffix = mistype[i + 1 :]
            for ch in ascii_lowercase:
                fixed = prefix + ch + suffix
                if fixed in properWords:
                    res.append(fixed)
                    break
    return res


def solution_louis(properWords, mistypes):
    hm = dict()
    for word in properWords:
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1 :]
            wildcard = prefix + "*" + suffix
            hm[wildcard] = word
    res = []
    for mistype in mistypes:
        for i in range(len(mistype)):
            prefix = mistype[:i]
            suffix = mistype[i + 1 :]
            wildcard = prefix + "*" + suffix
            if wildcard in hm.keys():
                res.append(hm[wildcard])
    return res
