def create_string_from_subsegment(subsegment):
    unique_chars = set()
    s = list()
    for char in subsegment:
        if char not in unique_chars:
            unique_chars.add(char)
            s.append(char)
    return ''.join(s)

def merge_the_tools(string, k):
    subsegments = [string[i*k:i*k+k] for i in range(len(string) // k)]
    for subsegment in subsegments:
        print(create_string_from_subsegment(subsegment))
