import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities = ['chicago', 'new york city', 'washington']
    global city
    city = str(input("please enter the name of the city as in ('chicago', 'new york city', 'washington'): ")).lower()
    while city not in cities:
        city = str(input("please enter the name of the city as in ('chicago', 'new york city', 'washington'): ")).lower()
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','july','august','september','october','november','december','all']
    month = str(input("please enter the month you want as (january , february,.....) or all: ")).lower()
   
    while month not in months :
         month = str(input("please enter the month you want as (january , february,.....) or all: ")).lower()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday','tuesday','wednesday','thursday','friday',"all"]
    day = str(input("please enter the day you want as in (saturday, monday....) or all: ")).lower()
    while day not in days :
        day = str(input("please enter the day you want as in (saturday, monday....) or all: ")).lower()

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
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time',"End Time"])
    df.drop('Unnamed: 0',inplace=True, axis = 1)
    if (month == "all") & (day == "all"):
        df = df 
    elif (month == "all") & (day != "all"):
        df = df[df["Start Time"].dt.day_name() == day.title()]
    elif (month != "all") & (day == "all"):
        df = df[df["Start Time"].dt.month_name() == month.title()]
    else:
        df = df[(df["Start Time"].dt.month_name() == month.title()) & (df["Start Time"].dt.day_name() == day.title())]

            


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ",df["Start Time"].dt.month_name().value_counts().index.tolist()[0])

    # TO DO: display the most common day of week
    print("The most common day is: ",df["Start Time"].dt.day_name().value_counts().index.tolist()[0])

    # TO DO: display the most common start hour
    print("The most common hour is: ", df["Start Time"].dt.hour.value_counts().index.tolist()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most common used start station is: ",df["Start Station"].value_counts().index.tolist()[0])

    # TO DO: display most commonly used end station
    print("\nThe most common end station: ",df["End Station"].value_counts().index.tolist()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("\nThe most frequent combination of start station and end station trip: ",df.groupby(["Start Station","End Station"]).size().sort_values(ascending=False).index.tolist()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\nThe total time travel is: {} seconds".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("\nThe avarage travel time is: {} seconds".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nThe user type counts are: ",df["User Type"].value_counts())

    # TO DO: Display counts of gender
    if city != "washington" :
        print("\nThe counts og gender are: ",df["Gender"].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earlist year of birt is: {} \nThe most recent year is: {} \n The common year of birth is: {} ".format(df["Birth Year"].min(),df["Birth Year"].max(),df["Birth Year"].value_counts().index.tolist()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while view_data not in ["yes","no"]:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    view_display = "yes"
    while (view_data == "yes") & (view_display == "yes"):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
