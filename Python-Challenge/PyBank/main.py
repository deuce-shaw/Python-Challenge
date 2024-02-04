import os
import csv

budget_data_csv = os.path.join('../Resources/budget_data.csv')

row_count = 0 

with open(budget_data_csv, 'r') as csvfile: 
    csv_reader = csv.reader(csvfile)

    next(csv_reader, None)

    for row in csv_reader: 
        row_count += 1

    print('Total Months:' + str(row_count))


net_total = 0.0

with open(budget_data_csv, 'r') as csvfile: 
    csv_reader = csv.reader(csvfile) 

    next(csv_reader, None) 

    for row in csv_reader: 
        try: 
            profit_loss = int(row[1])

            net_total += profit_loss

        except: 
            pass

    print('Total:' + '$' + str(net_total))

with open(budget_data_csv, 'r'): 
    csv_reader = csv.reader(csvfile)

    next(csv_reader, None)

    pl = []
    length = []
    change = []

    for row in csv_reader: 
        pl.append(int(row[1]))
        length.append(row[0])

    for i in range(1, len(pl)): 
        change.append((int(pl[i]) - int(pl[i-1])))

    pl_average = sum(change) / len(change)

    print('Average Change:' + '$' + str(round(pl_average)))

    pl_max = max(change)
    pl_min = min(change)

    print('Greatest Increase in Profit:' + '$' + str(pl_max))
    print('Greatest Decrease in Profit:' + '$' + str(pl_min))

    f = open('output.text', 'w')
    f.write('Financial Analysis' + '\n')
    f.write('...........................' + '\n')
    f.write('Total Months:' + str(row_count) = '\n')
    f.write('Total:' + '$' + str(net_total) = '\n')
    f.write('Average Change:' + '$' + str(round(pl_average)) + '\n')
    f.write('Greatest Increase in Profit:' + '$' + str(pl_max) + '\n')
    f.write('Greatest Decrease in Profit:' + '$' + str(pl_min))
    f.close()
