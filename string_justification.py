import sys
file_name = str(sys.argv[1])
width = int(sys.argv[2])
fp = open(file_name,'r')
string_list = fp.readlines()
def justify(string,width):
    try:
        if len(string) > width:
            raise ValueError()
        lenght_of_string = len(string)
        spaces = width - lenght_of_string
        list_of_words = string.split()
        if len(list_of_words) <= 1:
            raise ValueError()
        no_of_slots = len(list_of_words) - 1
        output = []
        remainder = spaces % no_of_slots
        for word in list_of_words:
            output.append(word)
            base_space = spaces//no_of_slots + 1
            if remainder > 0:
                base_space = base_space + 1
            output.append(base_space)
            remainder = remainder - 1
        final_output = ''
        # print(output[:-1])
        for k in output[:-1]:
            spa = ' '
            if str(k).isdigit():
                final_output = final_output + k*spa
            else:
                final_output = final_output + k
        print(final_output)
    except ValueError:
        print('Please check length of string')

for string in string_list:
    justify(string.strip(),width)