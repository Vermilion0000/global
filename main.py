calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()
    length = len(s)
    upper_case = s.upper()
    lower_case = s.lower()
    return (length, upper_case, lower_case)

def is_contains(s, list_to_search):
    count_calls()
    s_lower = s.lower()
    return any(s_lower in item.lower() for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
