import sys, ast
from statistics import mean, stdev

stats = []
results = []

with open(sys.argv[1]) as f:
    for line in f.readlines():
        if line[0:3] == 'c 1':
            data = [float(x) for x in line.split()[2:]]
            stats.append(data)
        elif line[0] == '{':
            if line.strip()[-1] == 'c':
                line = line.strip()[:-1]

            results.append(ast.literal_eval(line))

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
for g, p in experiments:
    conflicts = []
    level = []

    for result in experiments[(g, p)]:
        conflicts.append(result['conflicts'])
        level.append(result['level'])


    print('{} givens, {:.3f} inside: {:.2f} ({:.2f}) conflicts, {:.1f} ({:.1f}) level'.format(g, p, mean(conflicts), stdev(conflicts), mean(level), stdev(level)))
