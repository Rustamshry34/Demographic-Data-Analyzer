import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?

    average_age_men = df[df['sex'] == 'Male']['age'].astype(int).mean()

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)

    bachelors_count = len(df[df['education'] == 'Bachelors'])

    percentage_bachelors = (bachelors_count / total_people) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    AD = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

          #AD = AD[AD['Salary'] == '>50K'][['education', 'Salary',]]

    

    # What percentage of people without advanced education make more than 50K?
     
    Non_AD = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(AD)
    lower_education = len(Non_AD)
   
    Higherlen = len((AD['salary'] == '>50K'))
    lowerlen = len((Non_AD['salary'] == '>50K'))

    # percentage with salary >50K
    higher_education_rich = (Higherlen / higher_education) * 100
    lower_education_rich = (lowerlen / lower_education) * 100 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours = df[df['hours-per-week'] == min_work_hours]

    num_min_workers = (min_hours['salary'] == '>50K').sum()

    total_min_hours_people = len(min_hours)

    rich_percentage = (num_min_workers/ total_min_hours_people) * 100


    # What country has the highest percentage of people that earn >50K?
 
    salary_by_country = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    salary_by_country1 = salary_by_country['>50K'] * 100

    highest_earning_country = salary_by_country['>50K'].idxmax()
    highest_earning_country_percentage =  salary_by_country1.max()

    # Identify the most popular occupation for those who earn >50K in India.
    IndiaSalary= df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    Count_Occupation = IndiaSalary['occupation'].value_counts()

    top_IN_occupation = Count_Occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
