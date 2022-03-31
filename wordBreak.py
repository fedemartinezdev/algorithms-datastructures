def wordBreak(s, wordDict):
    memo = {}
    return naiveApproach(s, wordDict, memo)

"""
[car, ca, rs]
                cars
    s           rs              X
X  X  X      X  X  ""
"""
    
def naiveApproach(s, wordDict, memo):
    if s in memo:
        return memo[s]

    if s == "":
        return True

    for word in wordDict:
        word_len = len(word)
        if s[0:word_len] == word:
            suffix = s[word_len:]
            if naiveApproach(suffix, wordDict, memo):
                memo[suffix] = True
                return True

    memo[s] = False
    return False

print(wordBreak("cars", ['car','ca','rs']))
print(wordBreak("leetcode", ['leet','code','rs']))
print(wordBreak("applepenapple", ["apple","pen"]))
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))