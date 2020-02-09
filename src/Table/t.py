if __name__ == '__main__': 
    names = ['bar', 'chocolate', 'chips']
    weights = [0.05, 0.1, 0.25]
    costs = [2.0, 5.0, 3.0]
    unit_costs = [40.0, 50.0, 12.0]


    titles = ['names', 'weights', 'costs', 'unit_costs']
    data = [titles] + list(zip(names, weights, costs, unit_costs))
    print(data)

    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(12) for x in d)
        print(line)
        if i == 0:
            print('-' * len(line))