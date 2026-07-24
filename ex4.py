# Naive Pattern Searching Function
def search(pat, txt):
    n = len(txt)
    m = len(pat)
    result = []

    # Check every possible position
    for i in range(n - m + 1):
        j = 0

        while j < m:
            if txt[i + j] != pat[j]:
                break
            j += 1

        # If the entire pattern matched
        if j == m:
            result.append(i)

    return result


# Example Usage
txt = "AABAACAADAABAABA"
pat = "AABA"

result = search(pat, txt)

print("Pattern found at indices:", result)