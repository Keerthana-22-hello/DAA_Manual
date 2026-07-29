import time


# =====================================================
# Naive String Matching
# =====================================================

def naive_search(text, pattern):

    matches = []
    comparisons = 0

    start = time.perf_counter()

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        j = 0

        while j < m:

            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    execution_time = (
        time.perf_counter() - start
    ) * 1000

    return matches, comparisons, execution_time


# =====================================================
# KMP Helper (LPS Array)
# =====================================================

def compute_lps(pattern):

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:

                length = lps[length - 1]

            else:

                lps[i] = 0
                i += 1

    return lps


# =====================================================
# KMP Algorithm
# =====================================================

def kmp_search(text, pattern):

    matches = []
    comparisons = 0

    start = time.perf_counter()

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < len(text):

        comparisons += 1

        if text[i] == pattern[j]:

            i += 1
            j += 1

            if j == len(pattern):

                matches.append(i - j)

                j = lps[j - 1]

        else:

            if j != 0:

                j = lps[j - 1]

            else:

                i += 1

    execution_time = (
        time.perf_counter() - start
    ) * 1000

    return matches, comparisons, execution_time


# =====================================================
# Rabin-Karp Algorithm
# =====================================================

def rabin_karp(text, pattern):

    matches = []
    comparisons = 0

    start = time.perf_counter()

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    if m > n:
        return [], 0, 0

    h = 1

    for _ in range(m - 1):

        h = (h * d) % q

    pattern_hash = 0
    text_hash = 0

    for i in range(m):

        pattern_hash = (
            d * pattern_hash + ord(pattern[i])
        ) % q

        text_hash = (
            d * text_hash + ord(text[i])
        ) % q

    for i in range(n - m + 1):

        if pattern_hash == text_hash:

            match = True

            for j in range(m):

                comparisons += 1

                if text[i + j] != pattern[j]:

                    match = False
                    break

            if match:

                matches.append(i)

        if i < n - m:

            text_hash = (

                d * (text_hash - ord(text[i]) * h)

                + ord(text[i + m])

            ) % q

            if text_hash < 0:

                text_hash += q

    execution_time = (
        time.perf_counter() - start
    ) * 1000

    return matches, comparisons, execution_time


# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("Naive")
    print(naive_search(text, pattern))

    print()

    print("KMP")
    print(kmp_search(text, pattern))

    print()

    print("Rabin-Karp")
    print(rabin_karp(text, pattern))