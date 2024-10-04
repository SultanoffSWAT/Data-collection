import pandas as pd
import re

jobs = pd.read_csv(r"C:\Users\User\Downloads\archive\glassdoor_jobs.csv", delimiter=',')

jobs.drop(['Unnamed: 0'], axis=1, inplace = True)

# print("Total enteries : ",jobs.shape[0])
# print("Total attributes : ",jobs.shape[1])

jobs.describe(include = ['object', 'category'])

jobs.columns

jobs.drop(columns = ['Headquarters', 'Founded', 'Competitors', 'Job Description', 'Industry'], axis = 1, inplace = True)

jobs.head(3)

len(jobs[jobs.duplicated()])

jobs.drop_duplicates(inplace = True)

jobs.isna().sum()

def parse_salary(s):
    pattern = r"\$(\d+)(K)?-\$(\d+)(K)?"
    match = re.search(pattern, s)
    if match:
        num1, k1, num2, k2 = int(match.group(1)), match.group(2), int(match.group(3)), match.group(4)
        if k1 == 'K':
            value1 = num1 * 1000
        else:
            value1 = num1 * 2080
        if k2 == 'K':
            value2 = num2 * 1000
        else:
            value2 = num2 * 2080
        
        average = (value1 + value2) / 2
        return average
    else:
        return None
jobs['salary'] = jobs['Salary Estimate'].apply(parse_salary)

jobs[['Salary Estimate', 'salary']]

jobs.drop(columns = ['Salary Estimate'], axis = 1, inplace = True)

jobs['Job Title'].value_counts()

jobs['Company Name'] = jobs['Company Name'].str.slice(0, -4)

jobs.head(2)

print(jobs.columns)

highest_salary_per_sector = jobs.groupby('Sector')['salary'].max()

size_order = ["1 to 50 employees", "51 to 200 employees", "201 to 500 employees", "501 to 1000 employees",
              "1001 to 5000 employees", "5001 to 10000 employees", "10000+ employees"]
jobs['Size'] = pd.Categorical(jobs['Size'], categories=size_order, ordered=True)
biggest_companies = jobs[jobs['Size'] == '10000+ employees']

highest_paying_jobs = jobs[['Job Title', 'salary']].sort_values(by='salary', ascending=False).head(10)

highest_salary_per_sector, biggest_companies[['Company Name', 'Job Title', 'Size', 'salary']].head()