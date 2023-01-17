### Code to complete [START] ###

# Question 1

def line_count(filename):
    with open(filename, "r") as file:
        count = 0
        for line in file :
            count += 1
        return(count)

# Question 2

def char_count(filename):
    with open(filename, "r") as file:
        count_character = 0
        for line in file :
            for character in line :
                count_character += 1
        return(count_character)

# Question 3

def space(filename, n):
    with open(filename, "w") as file :
        for x in range(n):
            file.write(" ")

# Question 4

def capitalize(filename_in,filename_out):
    with open(filename_in, "r") as file_in:
        with open(filename_out, "w") as file_out:
            for line in file_in :
                line = line.upper()
                file_out.write(line)