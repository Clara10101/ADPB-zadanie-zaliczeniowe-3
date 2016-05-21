input_file = open("dane_z_galaxy.txt","r")
output_file = open("wynik_chromosomy.txt","w")

#Usrednienie sygnalu w ramach okien dlugosci 50kb

data = {"chr10":[],"chr11":[],"chr12":[]}

for line in input_file:
    current_line = line.split()
    chromosom = current_line[0]
    data[chromosom].append([current_line[1],current_line[2],current_line[3]])

data["hs10"] = data.pop("chr10")
data["hs11"] = data.pop("chr11")
data["hs12"] = data.pop("chr12")

for chromosom in data:

    start = int(int(data[chromosom][0][0]) / 50000) * 50000
    end = start + 50000
    value = 0
    n = 0
    for actual_list in data[chromosom]:

        actual_list_start = int(actual_list[0])
        actual_list_end = int(actual_list[1])
        actual_list_value = int(actual_list[2])

        if end < actual_list_start:

            if n > 0:
                output_file.write(chromosom + "\t" + str(start) + "\t" + str(end-1) + "\t" + str(value / n) + "\n")
            else:
                print "Wyniki z przedzialu " + str(start) + " - " + str(end) + " nie sa zawarte w pliku (" + chromosom + ")"

            value = 0
            n = 0
            start += 50000
            end += 50000

        elif end <= actual_list_end:

            value += (end - actual_list_start) * actual_list_value
            n += end - actual_list_start
            if n > 0:
                output_file.write(chromosom + "\t" + str(start) + "\t" + str(end-1) + "\t" + str(value / n) + "\n")

            #do nowego przedzialu
            value = (actual_list_end - end + 1) * actual_list_value
            n = actual_list_end - end + 1
            start += 50000
            end += 50000

        elif end > actual_list_end:

            #koniec wychodzi poza ten przedzial - dodanie wszystkich wartosci z tego przedzialu
            value += (actual_list_end - actual_list_start) * actual_list_value
            n += actual_list_end - actual_list_start


