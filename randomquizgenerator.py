#coding:utf-8

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quiznum in range(35):
    quizfile = open('capitalquiz%s.txt' % (quiznum + 1), "w")
    answerkeyfile = open('capitalquiz_answer%s.txt' % (quiznum+1), "w")

    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((''*20)+'state capital quiz(Form %s)' % (quiznum + 1))
    quizfile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for questionnum in range(50):
        correctanswer = capitals[states[questionnum]]
        wronganswers = list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers = random .sample(wronganswers,3)
        answeroptions = wronganswers +[correctanswer]
        random.shuffle(answeroptions)

        quizfile.write('%s.what is the capital of %s\n' % (questionnum+1,states[questionnum]))
        for i in range(4):
            quizfile.write('    %s. %s\n' % ('ABCD'[i], answeroptions[i]))
            quizfile.write('\n')
        answerkeyfile.write('%s. %s\n' % (questionnum + 1, 'ABCD'[answeroptions.index(correctanswer)]))
    quizfile.close()
    answerkeyfile.close()



