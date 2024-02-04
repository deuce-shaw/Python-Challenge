import os 
import csv 

election_data_csv = os.path.join('../Resources/election_data.csv')

with open(election_data_csv, 'r') as csvfile: 
    csv_reader = csv.reader(csvfile)

    next(csv_reader, None)

    total_votes = 0

    for row in csv_reader: 
        total_votes += 1
    print('Total Votes:' + str(total_votes))

with open(election_data_csv, 'r'): 
    csv_reader = csv.reader(csvfile)

    next(csv_reader, None)

    total_count_C = 0
    total_count_D = 0
    total_count_R = 0
    Candidate_C = ('Charles Casper Stockham')
    Candidate_D = ('Diana DeGette')
    Candidate_R = ('Raymon Anthony Doane')

    for row in csv_reader: 
        if row[2] == Candidate_C: 
            total_count_C += 1
        elif row[2] == Candidate_D: 
            total_count_D += 1
        elif row[2] == Candidate_R: 
            total_count_R += 1

    percent_vote_C = total_count_C / total_votes * 100
    percent_vote_D = total_count_D / total_votes * 100
    percent_vote_R = total_count_R / total_votes * 100

print(f'{Candidate_C}: {percent_vote_C:.3f}% ({total_count_C})')
print(f'{Candidate_D}: {percent_vote_D:.3f}% ({total_count_D})')
print(f'{Candidate_R}: {percent_vote_R:.3f}% ({total_count_R})')

if total_count_C > total_count_D and total_count_C > total_count_R: 
    winner = Candidate_C
elif total_count_D > total_count_C and total_count_D > total_count_R: 
    winner = Candidate_D
elif total_count_R > total_count_C and total_count_R > total_count_D: 
    winner = Candidate_R
print(f'Winner: {winner}')

with open('output.txt', 'w') as f: 
    f.write('Election Results\n')
    f.write('.........................\n')
    f.write(f'Total Votes: {total_votes}\n')
    f.write('..........................\n')
    f.write(f'{Candidate_C}: {percent_vote_C:.3f}% ({total_count_C})\n')
    f.write(f'{Candidate_D}: {percent_vote_D:.3f}% ({total_count_D})\n')
    f.write(f'{Candidate_R}: {percent_vote_R:.3f}% ({total_count_R})\n')
    f.write(f'..........................\n')
    f.write(f'Winner: {winner}\n')
    f.write(f'...........................\n')
f.close()