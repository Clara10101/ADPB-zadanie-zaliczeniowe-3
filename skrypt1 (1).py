input_file = open("interactions.txt","r")
output_file = open("wynik_interactions.txt","w")

def color_from_p_value(p_value):
    #kolor zalezny od p-value
    if p_value > 0.001:
        return 1
    elif 0.001 > p_value > 0.00001:
        return 2
    elif 0.00001 > p_value > 0.0000001:
        return 3
    elif 0.0000001 > p_value > 0.000000001:
        return 4
    else:
        return 5

def color_for_chromosom(chromosom):
    if chromosom == "hs10":
        return "blues"
    elif chromosom == "hs11":
        return "ylorrd"
    else:
        return "purples"

allowed_chromosomes = ["hs10","hs11","hs12"]

chromosom_interactions = {"hs10":([],[]),"hs11":([],[]),"hs12":([],[])}

for line in input_file:

    current_line = line.split()
    chromosom_1 = current_line[0]
    chromosom_2 = current_line[3]
    p_value = float(current_line[6])

    if chromosom_1 in allowed_chromosomes and chromosom_2 in allowed_chromosomes:

        if chromosom_1 != chromosom_2:
            output_file.write("\t".join(current_line[:-1]) + "\tcolor=" + color_for_chromosom(chromosom_1) + "-5-seq-" + str(color_from_p_value(p_value)) + ",thickness=2p" + "\n")
        else:
            if p_value < 0.00001:
                chromosom_1_start = float(current_line[1]); chromosom_1_end = float(current_line[2])
                chromosom_2_start = float(current_line[4]); chromosom_2_end = float(current_line[5])
                distance = abs((chromosom_1_start + chromosom_1_end)/2 - (chromosom_2_start + chromosom_2_end)/2)
                chromosom_interactions[chromosom_1][0].append("\t".join(current_line[:-1]) + "\tcolor=" + color_for_chromosom(chromosom_1) + "-5-seq-" + str(color_from_p_value(p_value)) + ",thickness=2p")
                chromosom_interactions[chromosom_1][1].append(distance)

#dla kazdego chromosomu wybranie 500 najlepszych interakcji
for chrom in chromosom_interactions:
    best_distance = sorted(range(len(chromosom_interactions[chrom][1])), key=lambda x: chromosom_interactions[chrom][1][x])[-500:]
    for i in best_distance:
        output_file.write(chromosom_interactions[chrom][0][i]+"\n")