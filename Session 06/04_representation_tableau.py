# Guillaume Gillard

### Code to complete [START] ###

def table(filename_in, filename_out, width):
    bar = "+" + "-"*(width+2) + "+\n"
    with open(filename_in, "r") as file_in :
        with open(filename_out, "w") as file_out :
            file_out.write(bar)
            for word in file_in :
                word = word.strip()
                if len(word) < width :
                    word = word + (" " * (width-len(word)))
                file_out.write("| " + word[:width] + " |\n")
            file_out.write(bar.strip())
            return
