import sys

from datetime import date

today = date.today()

import file_input
import showtimes

def main():
    if len(sys.argv) < 2:
        print('Please specify a input file.')
        return

    file_path = sys.argv[1]

    movies = file_input.get_movies_from_file(file_path)

    print(today.strftime("\n%A %x")) # maybe make the year right

    for movie in movies:
        print(f"\n{movie['title']} - Rated {movie['rating']}, {movie['runtime']}")
        show_times = showtimes.generate_showtimes(today,movie['runtime'])
        for showtime in show_times:
            print(showtime)

if __name__ == "__main__":
    main()
