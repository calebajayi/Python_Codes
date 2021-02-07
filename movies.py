class Movie():
    def __init__(self, name, year_release):
        self._name = name
        self._year = year_release
        self._onloan = False

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Title: '+self._name+' On loan: ' + str(self._onloan)


class User():
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


def find_movie(list_movies, movie_name):
    for m in list_movies:
        if m.get_name() == movie_name:
            return m

    print('No such movie')
    return None


movies = [Movie('Spiderman', 2018), Movie('Starwars', 2017), Movie('Ironman', 2015)]
users = [User('John'), User('Ann'), User('Peter'), User('Mary')]

person_name = input('Enter person\'s name :')
movie_name = input('Enter movie\'s name :')
p = find_user(users, person_name)
m = find_movie(movies, movie_name)

p.loan_movie(m)

for m in movies:
    print(m)

for u in users:
    print(u)
