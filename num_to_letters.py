nums_to_letters = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

def generate_combinations(num_string):
    return generate_helper(num_string, '')

def generate_helper(num_string, string_so_far):
    if not num_string:
        print(num_string)
        return
    current = num_string[0]
    if len(num_string) == 1:
        for char in nums_to_letters[current]:
            print(string_so_far + char)
        return 
    if current in nums_to_letters:
        for char in nums_to_letters[current]:
            generate_helper(num_string[1:], string_so_far + char)
    else:
        generate_helper(num_string[1:], string_so_far + current)

if __name__ == '__main__':
    generate_combinations('79849664')
