# Input: "banana"
# Output: "a3b1n2"


def freq_count(txt):
    data = {}
    for ch in txt:
        data[ch] = data.get(ch, 0) + 1

    result = ''
    for ch in sorted(data.keys()):
        result += ch + str(data[ch])
    return result
print(freq_count('ashutoshpradhan'))
