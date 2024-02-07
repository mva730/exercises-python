def find_mistake(original_str, mistaken_str, mistakes=0):
    # if mistakes > 1:
    #     return mistakes

    if original_str == mistaken_str:
        return 0
    if len(original_str) == 1 and original_str != mistaken_str:
        mistakes += 1
        return mistakes

    middle = len(original_str) // 2

    r = ""

    if original_str[:middle] != mistaken_str[:middle]:
        mistakes = find_mistake(original_str[:middle], mistaken_str[:middle], mistakes)

    if original_str[middle:] != mistaken_str[middle:]:
        mistakes = find_mistake(original_str[middle:], mistaken_str[middle:], mistakes)

    return mistakes


result = find_mistake('zxcv', 'aasd')

print(result)
