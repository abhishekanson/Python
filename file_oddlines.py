src = "source.txt"
dst = "destination.txt"

with open(src, "r") as f1, open(dst, "w") as f2:
    for line_number, line in enumerate(f1, start=1):
        if line_number % 2 == 1:
            f2.write(line)

print("Odd lines copied successfully!")
