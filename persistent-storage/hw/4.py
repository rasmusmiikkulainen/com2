def filter_file(filename_in, filename_out, cond):
    try:
        with open(filename_in, "r") as f_in, open(filename_out, "w") as f_out:
            for line in f_in:
                try:
                    if cond(line.rstrip()):
                        print(line, file=f_out, end="")
                except:
                    print("cond failed, skipping line")
    except Exception as e:
        print("exception:", e)
        return False

# remember to cd persistent-storage
filter_file("test.txt", "out.txt", str.isnumeric)
