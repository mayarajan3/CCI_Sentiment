import json
import matplotlib.pyplot as plt
import statistics

with open('average_scores_atlanta.json') as f:
  d = json.load(f)

npuA = dict(list(d.items())[0:11])
npuB = dict(list(d.items())[11:27])
npuC = dict(list(d.items())[27:50])
npuD = dict(list(d.items())[50:57])
npuE = dict(list(d.items())[57:68])
npuF = dict(list(d.items())[68:75])
npuG = dict(list(d.items())[75:88])
npuH = dict(list(d.items())[88:104])
npuI = dict(list(d.items())[104:123])
npuJ = dict(list(d.items())[123:129])
npuK = dict(list(d.items())[129:134])
npuL = dict(list(d.items())[134:136])
npuM = dict(list(d.items())[136:140])
npuN = dict(list(d.items())[140:147])
npuO = dict(list(d.items())[147:151])
npuP = dict(list(d.items())[151:184])
npuQ = dict(list(d.items())[184:186])
npuR = dict(list(d.items())[186:193])
npuS = dict(list(d.items())[193:200])
npuT = dict(list(d.items())[200:207])
npuV = dict(list(d.items())[207:213])
npuW = dict(list(d.items())[213:224])
npuX = dict(list(d.items())[224:229])
npuY = dict(list(d.items())[229:238])
npuZ = dict(list(d.items())[238:])
#duplicate names: Bankhead, Wildwood

npuDictionaries = {"NPU A": npuA, "NPU B": npuB, "NPU C": npuC, "NPU D": npuD, "NPU E": npuE, "NPU F": npuF,
"NPU G": npuG, "NPU H": npuH, "NPU I": npuI, "NPU J": npuJ, "NPU K": npuK, "NPU L": npuL, "NPU M": npuM, "NPU N": npuN,
"NPU O": npuO, "NPU P": npuP, "NPU Q": npuQ, "NPU R": npuR, "NPU S": npuS, "NPU T": npuT, "NPU V": npuV, "NPU W": npuW,
"NPU X": npuX, "NPU Y": npuY, "NPU Z": npuZ}

overall_values = []

amin = 100
amax = -1
amin_key = None
amax_key = None

max_avg = -1
min_avg = 100
min_avg_key = None
max_avg_key = None

max_range = 0
min_range = 100
min_range_key = None
max_range_key = None

max_stdv = 0
min_stdv = 100
min_stdv_key = None
max_stdv_key = None

count = 0

print("NPU-WIDE RESULTS")
for name, dictionary in npuDictionaries.items():
    cleanDictionary = {}
    keys = dictionary.keys()
    for key in keys:
        if dictionary[key] != None:
            cleanDictionary[key] = dictionary[key]

    keys = list(cleanDictionary.keys())
    values = list(cleanDictionary.values())

    overall_values = overall_values + values
    count = count + len(values)

    max_sent = -1
    max_key = None
    min_sent = 2
    min_key = None

    average = 0


    for i in range(len(values)):
        if values[i] < min_sent:
            min_sent = values[i]
            min_key = keys[i]
        if values[i] > max_sent:
            max_sent = values[i]
            max_key = keys[i]
        average = average + values[i]

        if values[i] <= amin:
            amin = values[i]
            amin_key = keys[i]
        if values[i] > amax:
            amax = values[i]
            amax_key = keys[i]

    average = average/len(values)
    if (len(values)) >= 2:
        stdev = statistics.stdev(values)
    else:
        stdev = 0
    trange = max_sent - min_sent

    if stdev < min_stdv:
        min_stdv = stdev
        min_stdv_key = name
    if stdev >= max_stdv:
        max_stdv = stdev
        max_stdv_key = name

    if trange < min_range:
        min_range = trange
        min_range_key = name
    if trange >= max_stdv:
        max_range = trange
        max_range_key = name

    if average < min_avg:
        min_avg = average
        min_avg_key = name
    if average >= max_stdv:
        max_avg = average
        max_avg_key = name

    print(name)
    print("Max sentiment neighborhood: ", max_key, ": ", max_sent)
    print("Min sentiment neighborhood: ", min_key, ": ", min_sent)
    print("Standard deviation: ", stdev)
    print("Range: ", trange)
    print("Average sentiment: ", average)
    print("Number of tweets: ", len(values))
    print()
    plt.bar(keys, values)
    plt.title(name)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('results/graphs/' + name + '.png')
    plt.clf()

plt.boxplot(values, vert=False)
plt.title("All Sentiments")
plt.savefig('results/graphs/boxplot.png')
plt.clf()

print("ATLANTA-WIDE RESULTS")
print("Average: ", sum(overall_values)/count)
print("Max neighborhood: ", amax, ": ", amax_key)
print("Min neighborhood: ", amin, ": ", amin_key)
print()
print("Max average NPU: ", max_avg, ": ", max_avg_key)
print("Min average NPU: ", min_avg, ": ", min_avg_key)
print()
print("Max stdev NPU: ", max_stdv, ": ", max_stdv_key)
print("Min stdev NPU: ", min_stdv, ": ", min_stdv_key)
print()
print("Max range NPU: ", max_range, ": ", max_range_key)
print("Min range NPU: ", min_range, ": ", min_range_key)





