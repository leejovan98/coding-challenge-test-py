from collections import defaultdict
from string import ascii_lowercase


class Trie:
    def __init__(self):
        self.dict = {}

    def __repr__(self):
        return str(self.dict)

    def add_word(self, word):
        trie_node = self
        for ch in word:
            if ch not in trie_node.dict:
                trie_node.dict[ch] = Trie()
            trie_node = trie_node.dict[ch]
        trie_node.dict["is_terminal"] = True

    # ret (true, word)
    def find_word(self, mistyped, num_err):
        if not mistyped:
            return "is_terminal" in self.dict, ""
        first_ch = mistyped[0]
        if first_ch in self.dict:
            ok, substr = self.dict[first_ch].find_word(mistyped[1:], num_err)
            if ok:
                return (ok, first_ch + substr)
        if num_err < 1:
            for char, trie_node in self.dict.items():
                if char == first_ch:
                    continue
                ok, substr = trie_node.find_word(mistyped[1:], num_err + 1)
                if ok:
                    return (ok, char + substr)
        return (False, "")


def solution_trie(proper_words, mistypes):
    trie = Trie()
    for word in proper_words:
        trie.add_word(word)
    res = []
    for mistype in mistypes:
        ok, fixed = trie.find_word(mistype, 0)
        if ok:
            res.append(fixed)
    return res


def solution_adhy(properWords, mistypes):
    def fix_word(properWords, mistype):
        for i in range(len(mistype)):
            prefix = mistype[:i]
            suffix = mistype[i + 1 :]
            for ch in ascii_lowercase:
                fixed = prefix + ch + suffix
                if fixed in properWords:
                    return fixed

    properWords = set(properWords)
    res = []
    for mistype in mistypes:
        fixed = fix_word(properWords, mistype)
        if fixed:
            res.append(fixed)
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
