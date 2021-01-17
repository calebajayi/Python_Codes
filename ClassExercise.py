class Movies:
    def __init__(self, name, year_release):
        self._name = name
        self._year = year_release
        self._onloan = False

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Title: '+self._name+' On loan: '+str(self._onloan)


class Users:
    def __init__(self, name):
        self._name = name
        self._movie = None

    def get_name(self):
        return self._name

    def loan_movie(self, m):
        self._movie = m
        m._onloan = True

    def __str__(self):
        return 'Name: '+self._name+' Movies on loan: ' + str(self._movie)


def find_user(list_users, user_name):
    for u in list_users:
        if u.get_name() == user_name:
            return u

    print('No such user')
    return None


def find_movie(list_movie, movie_name):
    for m in list_movie:
        if m.get_name() == movie_name:
            return m

    print('No such movie')
    return None


Movies = [Movies('Spiderman', 2018), Movies('Starwars', 2017), Movies('Ironman', 2015)]

Users = [Users('John'), Users('Ann'), Users('Peter'), Users('Mary')]

#loan a movie
#u1.loan_movie(m1)

#u = find_user(Users, 'Ann')
#print(u)

#for m in Movies:
#    print(m)

#for u in Users:
#    print(u)

person_name = input('Enter person name:')
movie_name = input('Enter movie name:')
p = find_user(Users, person_name)
m = find_movie(Movies, movie_name)

p.loan_movie(m)

for m in Movies:
    print(m)

for u in Users:
    print(u)
