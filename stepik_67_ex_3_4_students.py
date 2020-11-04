
# Create three variables to store the total of points in math, physics, russian
total_math = 0
total_physics = 0
total_russian = 0

# Create variable to count the number of students
# It will be used later to calculate the average
counter = 0

# Open, read, split into separate pieces
with open("dataset_3363_4.txt", 'r') as fh, open("output_3363_4.txt", 'w') as fout:

    # Split every line in words by ";" and store as list
    for line in fh:
        line = line.strip().split(';')
        total_math += int(line[1])
        total_physics += int(line[2])
        total_russian += int(line[3])
        individual_avg = (int(line[1]) + int(line[2]) + int(line[3])) / 3
        fout.write(str(individual_avg) + '\n')
        counter += 1

    avg_math = total_math / counter
    avg_physics = total_physics / counter
    avg_russian = total_russian / counter

    fout.write(str(avg_math) + " " + str(avg_physics) + " " + str(avg_russian) + '\n')
