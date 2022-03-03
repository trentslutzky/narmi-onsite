import csv

fieldnames = [
        'title',
        'year',
        'rating',
        'runtime'
]

def get_movies_from_file(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file,fieldnames)
        movies = list(reader)
        movies.pop(0)
        return movies

def main():
    get_movies_from_file('./test_files/01_test_example.txt')

if __name__ == "__main__":
    main()
