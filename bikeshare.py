import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 'january': 0,'february': 1,'march': 2,'april': 3,'may': 4,'june': 5, 'all' : 6}

DAY_DATA = { 'monday': 0,'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday': 5,'sunday': 6, 'all': 7}

"""City, Month and Day lists used for while loops during imputs"""

city_list = list(CITY_DATA.keys())
month_list = list(MONTH_DATA.keys())
day_list = list(DAY_DATA.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Would you like to look at chicago, new york city or washington?\n").lower()
    while city not in city_list:
         city = input("Invalid response, please try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month would you like to look at? For example \'january\', \'february\', or \'all\' for every month\n").lower()
    while month not in month_list:
        month = input("Invalid response, please try again.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("And what day of the week? For example \'sunday\', \'monday\' or \'all\' for every day\n").lower()
    while day not in day_list:
        day = input("Invalid response, please try again.\n")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month, day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print("The most popular day is ", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station is ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station is ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print("The most popular trip is ", popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time is ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_total = df['User Type'].value_counts().to_frame()
    print("The total amount of users per type is:\n", user_total)


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts().to_frame()
        print('The number of users per gender are:\n', gender_count)
    except KeyError:
        print("\nGender Count Data Not Available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        earliest_birthyear = int(earliest_birthyear)
        print("The oldest user was born in ", earliest_birthyear)
    except KeyError:
        print("Birth Year Data Not Available.")

    if 'Birth Year' in df.columns:
        recent_birthyear = df['Birth Year'].max()
        recent_birthyear = int(recent_birthyear)
        print("The youngest user was born in ", recent_birthyear)

    if 'Birth Year' in df.columns:
        common_birthyear = df['Birth Year'].mode()[0]
        common_birthyear = int(common_birthyear)
        print("The most common birth year is ", common_birthyear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Asks user if they would like to see the first 5 lines of raw data. Continues to loop if user inputs 'yes'. Stops when user inputs "no' """
    start_time = time.time()
    raw = np.array([0,1,2,3,4])
    while True:
        user_input = input("Would you like to see the raw data? Enter yes or no.\n")
        if user_input.lower() != "yes":
            break
        if user_input.lower() == "yes":
            print(df.iloc[raw])
            raw += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
