import sys, ast
from statistics import mean, stdev

stats = []
results = []

for a in sys.argv[1:]:
    with open(a) as f:
        for line in f.readlines():
            if line[0:3] == 'c 1':
                data = [float(x) for x in line.split()[2:]]
                stats.append(data)
            elif line[0] == '{':
                if line.strip()[-1] == 'c':
                    line = line.strip()[:-1]

                results.append(ast.literal_eval(line))

# print(len(results), len(stats))

for i in range(len(results)):
    results[i]['time'] = stats[i][0]
    results[i]['level'] = stats[i][1]
    results[i]['variables'] = int(stats[i][2])
    results[i]['used'] = stats[i][3]
    results[i]['original'] = int(stats[i][4])
    results[i]['conflicts'] = int(stats[i][5])
    results[i]['learned'] = int(stats[i][6])
    results[i]['limit'] = int(stats[i][7])
    results[i]['agility'] = stats[i][8]
    results[i]['memory'] = stats[i][9]

# Experiment aggregation
experiments = {}

for result in results:
    g = result['givens']
    p = result['proportion']

    if (g, p) not in experiments:
        experiments[(g, p)] = []

    experiments[(g, p)].append(result)

# Data processing
terms = ['givens', 'proportion', 'inside', 'outside', 'level', 'variables', 'used', 'original', 'conflicts', 'learned', 'limit', 'agility', 'memory']

print(','.join(terms[:4]), end=',')
print(','.join(['{},{}'.format(term, term+'-dev') for term in terms[4:]]))

for g, p in experiments:
    stats = {}
    output = '{},{:.2f},'.format(g, p)
    for stat in terms[2:]:
        accumulator = []
        for result in experiments[(g, p)]:
            accumulator.append(result[stat])

        m = mean(accumulator)
        s = stdev(accumulator)

        if stat != 'inside' and stat != 'outside':
            output += '{:.2f},{:.2f},'.format(m, s)
        else:
            output += '{:.2f},'.format(m)

    print(output[:-1])
