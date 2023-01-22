def find_common_substring(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:min(len(str1), len(str2))]