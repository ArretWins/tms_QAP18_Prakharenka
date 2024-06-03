#Тема проекта: приложение «Касса кинотеатра».
#Спроектировать ПО, предназначенное для автоматизации деятельности кассы кинотеатра. Функции, которые
#должны быть реализованы в приложении: добавление, удаление, редактирование и
#просмотр информации о сеансах, наличии билетов и свободных мест.

class Cinema:
    def __init__(self, name, count_of_movies, count_of_rooms):
        self.name = name
        self.count_of_movies = count_of_movies
        self.count_of_rooms = count_of_rooms
        self.movies = {}
        self.screenings = []

    def add_movie(self, title, duration, genre):
        self.movies[title] = {'duration': duration, 'genre': genre}
        self.count_of_movies = self.count_of_movies + 1

    def del_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self.count_of_movies = self.count_of_movies - 1

    def add_screening(self, title, room_number, time, seats):
        if title in self.movies:
            self.screenings.append(
                {
                    'title': title,
                    'room_number': room_number,
                    'time': time,
                    'seats': seats,
                    'booked_seats': 0
                }
            )

    def del_screening(self, title, time):
        self.screenings = [s for s in self.screenings if not (s['title'] == title and s['time'] == time)]

    def list_screenings(self):
        for screening in self.screenings:
            available_seats = screening['seats'] - screening['booked_seats']
            print(
                f"{screening['title']} at {screening['time']} in room {screening['room_number']}, {available_seats} seats available")


class TicketOffice:
    def __init__(self, cinema):
        self.cinema = cinema

    def book_seat(self, title, time, count=1):
        for screening in self.cinema.screenings:
            if screening['title'] == title and screening['time'] == time:
                if screening['booked_seats'] + count <= screening['seats']:
                    screening['booked_seats'] += count
                    print(f'U booked {count} seat(s) for {title} at {time}')
                    return True
                else:
                    print(f'Not enough available seats for {title} at {time}')
                    return False
        print(f'Screening not found for {title} at {time}')
        return False

    def return_tickets(self, title, time, count=1):
        for screening in self.cinema.screenings:
            if screening['title'] == title and screening['time'] == time:
                if screening['booked_seats'] - count >= 0:
                    screening['booked_seats'] -= count
                    print(f'U returned {count} ticket(s) for {title} at {time}')
                    return True
                else:
                    print(f'Cannot return {count} ticket(s) for {title} at {time}')
                    return False
        print(f'Screening not found for {title} at {time}')
        return False


cinema = Cinema('Optima', 2, 3)
cinema.add_movie('Bad boys', 220, 'Criminal')
cinema.add_movie('Invalid', 190, 'Comedy')

cinema.add_screening('Bad boys', 2, '19:00', 100)
cinema.add_screening('Invalid', 1, '22:00', 100)

ticket_office = TicketOffice(cinema)

cinema.list_screenings()
ticket_office.book_seat('Invalid', "22:00", 2)
ticket_office.book_seat('Bad boys', "19:00", 4)
ticket_office.book_seat('Bad boys', "19:00", 6)
cinema.list_screenings()

ticket_office.book_seat('Bad boys', "22:00", 6)
ticket_office.book_seat('Avatar', "22:00", 6)
