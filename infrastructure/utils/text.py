def camel_case_to_snake_case(input_str: str, plurize_word: bool = True) -> str:
    chars = []
    for char_index, char in enumerate(input_str):
        if char_index and char.isupper():
            next_index = char_index + 1

            flag = next_index >= len(input_str) or input_str[next_index].isupper()
            previous_char = input_str[char_index - 1]
            if previous_char.isupper() and flag:
                pass
            else:
                chars.append("_")

        chars.append(char.lower())

    result = "".join(chars)

    if plurize_word:
        result = plurize(result)
    return result


def plurize(word: str) -> str:
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    elif word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    else:
        return word + "s"