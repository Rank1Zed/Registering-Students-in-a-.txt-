from pathlib import Path
import os

def clear():
    os.system('cls')

while True:
    try: 
        user = int(input('How many students do you want to register?: '))
        break
    except ValueError:
        print('     Only integers numbers Please \'_\'')

quant = user

''' If you don't want to keep registering students, just remove this hashtag and the next hashtag.

# Where you can register the students below

Students_List = []

for _ in range(quant):
    Grade = []
    Name = str(input('Name: '))
    Subject = str(input('Subject: '))
    
    for i in range(1, 5):
        Grade = float(input(f'Grade {i}: '))
        Grade.append(Grade)

    aluno1 = {'Name': Name, 'Subject': Subject, 'Grade': Grade}

    Students_List.append(aluno1)   
    print('\n')     

aluno2 = {'Name': Name, 'Subject': Subject, 'Grade': Grade}

'''

#clear() # Clear Terminal
print('\n'*2) 

# remove the hashtag below if you haven't removed the two hashtags above

Students_List = [{'Name': 'Nicholas', 'Subject': 'Mathematics', 'Grade': [10.0, 7.0, 7.0, 9.0]}, {'Name': 'Roberto', 'Subject': 'Science', 'Grade': [4.0, 10.0, 9.0, 8.0]}, {'Name': 'Pedrinho', 'Subject': 'Quantum Physics', 'Grade': [4.0, 4.0, 0.0, 0.0]}, {'Name': 'Joaninha', 'Subject': 'Physics', 'Grade': [5.0, 6.0, 9.0, 7.0]}, {'Name': 'Alex', 'Subject': 'Alfred', 'Grade': [3.0, 4.0, 6.0, 1.0] }]

# Show the registration

for i in range(0, quant):

    n = Students_List[i]['Grade']
    sum = 0
    situation = ''

    for s in range(0, 4):
        sum += n[s]

    Average = sum / 4
    
    if Average >= 7:
        situation = 'Approved'
    elif Average < 7 and Average >= 4:
        situation = 'Recovery'
    elif Average < 4:
        situation = 'Failed'

    print(f'Name: ', Students_List[i]['Name'])
    print(f'Subject: ', Students_List[i]['Subject'])
    print(f'Grade: ', end='')
    
    string = ''

    for t in range(0, 3):
        string += str(n[t])
        string += ', '
    print(f'{string[:-2]} e {n[-1]}')

    print(f'Average: ', Average)
    print(f'Situation: ', situation, '\n')

# Writes the data to the document

directory = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(directory, "alunos.txt")

with open(data, "a", encoding="utf-8") as f:

    for i in range(0, quant):
        n = Students_List[i]['Grade']
        sum = 0
        situation = ''

        for s in range(0, 4):
            sum += n[s]

        Average = sum / 4
        
        if Average >= 7:
            situation = 'Approved'
        elif Average < 7 and Average >= 4:
            situation = 'Recovery'
        elif Average < 4:
            situation = 'Failed'

        f.write(f"Name: {Students_List[i]['Name']}\n")
        f.write(f"Subject: {Students_List[i]['Subject']}\n")
        f.write('Grade: ')
        
        string = ''

        for t in range(0, 3):
            string += str(n[t])
            string += ', '
        f.write(f'{string[:-2]} e {n[-1]}\n')

        f.write(f'Average: {Average}\n')
        f.write(f'Situation: {situation}')
        f.write('\n \n')