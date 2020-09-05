# Linear Seach implementation using Python
class Passenger(object):
    def __init__(self, name, home_country, travel_country, duration_of_stay):
        self.name=name
        self.home_country=home_country
        self.travel_country=travel_country
        self.duration_of_stay=duration_of_stay
    def __str__(self):
        return f"{self.name} from {self.home_country} going to {self.travel_country} for {self.duration_of_stay} days."

def search_passenger(passenger_name, passenger_list):
    for p in passenger_list:
        if passenger_name in getattr(p, 'name'):
            print(p)
            break # not to look any further
    else:
        print('Not found!')

passenger_list=[]
while(True):
    choice=input('Add a new passenger?(Y/N) :')
    if choice in ('Y','y'):
        name=input('Enter Name: ')
        home_country=input('Enter Home Country: ')
        travel_country=input('Enter Travel Country: ')
        duration_of_stay=input('Enter Duration of Stay(in digits): ')
        try:
            duration_of_stay=int(duration_of_stay)
        except:
            print('Duration of stay should be a number; Duration set to 0')
            duration_of_stay=0
        new_passenger=Passenger(name, home_country, travel_country, duration_of_stay)
        passenger_list.append(new_passenger)
    else:
        break

passenger_name=input('Enter a name to Search: ')
search_passenger(passenger_name, passenger_list)