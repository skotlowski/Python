projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for date, project, leader in zip(dates, projects, leaders):
    print(f'The leader of {project} started {date} is {leader}')


for number, (date, project, leader) in enumerate(zip(dates, projects, leaders)):
    print(f'{number} - The leader of {project} started {date} is {leader}')
