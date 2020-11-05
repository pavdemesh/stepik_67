import csv

tot_height_per_class = {i: 0 for i in range(1, 12)}
tot_stud_per_class = {j: 0 for j in range(1, 12)}

with open(r'dataset_3380_5.txt', 'r') as fh:

    tsv_read = csv.reader(fh, delimiter="\t")

    for row in tsv_read:
        st_class, st_name, st_height = int(row[0]), row[1], int(row[2])
        tot_height_per_class[st_class] += st_height
        tot_stud_per_class[st_class] += 1

with open("output_class.txt", 'w') as fout:

    for i in range(1, 12):
        if tot_stud_per_class[i] == 0:
            fout.write(str(i) + ' -' + '\n')
        else:
            avg_height = tot_height_per_class[i] / tot_stud_per_class[i]
            fout.write(str(i) + ' ' + str(avg_height) + '\n')
