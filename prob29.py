# Initial input sollection section
initial_input = input('initial state: ');
pw_11 = int(input());
pw_1000 = int(input());
input_arr = [];

# Collects additional input until input of 0
get_input = True;
while get_input:
    new_input = input();
    if new_input == '0':
        get_input = False;
    else:
        input_arr.append(new_input);

# Function to compute the value of a string for password
# Computed by adding the indexes of all characters in a string of character '#'
def compute_password(str, fval):
    sum = 0;
    for i in range(0, len(str)):
        if str[i] == '#':
            sum += fval + i;
    print(sum);

# Value to hold the value of the first char in string
firstval = 0;
proc_input = initial_input;
last_input = "placeholder";


for x in range(1001):
    standex = proc_input.index('#');
    lastdex = proc_input.rindex('#');
    new_length = len(proc_input);

    for i in range(4 - standex):
        temp_str = '.' + proc_input;
        proc_input = temp_str;
        # Increments first value down for every . added before it
        firstval -= 1;

    for i in range(4 - (new_length - (lastdex + 1))):
        temp_str = proc_input + '.';
        proc_input = temp_str;

    new_length = len(proc_input);

    # Array to hold all of the chars for next iteration
    temp_arr = ['.'] * new_length;

    for i in input_arr:
        temp_length = len(i);
        for a in range(len(proc_input) - (temp_length - 1)):
            if proc_input[a:a+temp_length] == i:
                temp_arr[a + int(temp_length / 2)] = '#';

    proc_input = "";
    for i in temp_arr:
        proc_input += i;

    if proc_input.find(last_input) != -1:
        dif = 50000000 - (x + 1);

    if x == 1000:
        compute_password(proc_input, firstval);

    last_input = proc_input;
    
