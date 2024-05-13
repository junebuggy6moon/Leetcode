def roman_to_i(roman_character):
    roman_character = roman_character.upper()
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    answer = 0
    for index in range(len(roman_character)):
        if index == len(roman_character) - 1:
            answer += map[roman_character[index]]
        else:
            if map[roman_character[index]] < map[roman_character[index + 1]]:
                answer -= map[roman_character[index]]
            else:
                answer += map[roman_character[index]]
    return answer

