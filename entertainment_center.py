import fresh_tomatoes
import media

# data structure with the 10 best movies ever according to imdb.com
movies_params = [
    {
        'title': 'The Shawshank Redemption',
        'year': '1994',
        'storyline': """Two imprisoned men bond over a number of years,
                     finding solace and eventual redemption through acts
                     of common decency.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=6hB3S9bIaco',
        'imdb_rating': '9.3',
        'imdb_url': 'http://www.imdb.com/title/tt0111161'
    },
    {
        'title': 'The Godfather',
        'year': '1972',
        'storyline': """The aging patriarch of an organized crime dynasty
                     transfers control of his clandestine empire to his
                     reluctant son.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=sY1S34973zA',
        'imdb_rating': '9.2',
        'imdb_url': 'http://www.imdb.com/title/tt0068646'
    },
    {
        'title': 'The Godfather: Part II',
        'year': '1974',
        'storyline': """The early life and career of Vito Corleone in 1920s
                     New York City is portrayed, while his son, Michael,
                     expands and tightens his grip on the family crime
                     syndicate.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR3,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=9O1Iy9od7-A',
        'imdb_rating': '9.0',
        'imdb_url': 'http://www.imdb.com/title/tt0071562'
    },
    {
        'title': 'The Dark Knight',
        'year': '2008',
        'storyline': """When the menace known as the Joker emerges from his
                     mysterious past, he wreaks havoc and chaos on the people
                     of Gotham, the Dark Knight must accept one of the
                     greatest psychological and physical tests of his ability
                     to fight injustice.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=EXeTwQWrcwY',
        'imdb_rating': '9.0',
        'imdb_url': 'http://www.imdb.com/title/tt0468569'
    },
    {
        'title': '12 Angry Men',
        'year': '1957',
        'storyline': """A jury holdout attempts to prevent a miscarriage of
                     justice by forcing his colleagues to reconsider the
                     evidence.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=A7CBKT0PWFA',
        'imdb_rating': '8.9',
        'imdb_url': 'http://www.imdb.com/title/tt0050083'
    },
    {
        'title': 'Schindler\'s List',
        'year': '1993',
        'storyline': """In German-occupied Poland during World War II, Oskar
                     Schindler gradually becomes concerned for his Jewish
                     workforce after witnessing their persecution by the Nazi
                     Germans.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=gG22XNhtnoY',
        'imdb_rating': '8.9',
        'imdb_url': 'http://www.imdb.com/title/tt0108052'
    },
    {
        'title': 'The Lord of the Rings: The Return of the King',
        'year': '2003',
        'storyline': """Gandalf and Aragorn lead the World of Men against
                     Sauron\'s army to draw his gaze from Frodo and Sam as they
                     approach Mount Doom with the One Ring.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=r5X-hFf6Bwo',
        'imdb_rating': '8.9',
        'imdb_url': 'http://www.imdb.com/title/tt0167260'
    },
    {
        'title': 'Pulp Fiction',
        'year': '1994',
        'storyline': """The lives of two mob hitmen, a boxer, a gangster\'s
                     wife, and a pair of diner bandits intertwine in four
                     tales of violence and redemption.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=s7EdQ4FqbhY',
        'imdb_rating': '8.9',
        'imdb_url': 'http://www.imdb.com/title/tt0110912'
    },
    {
        'title': 'Il buono, il brutto, il cattivo',
        'year': '1966',
        'storyline': """A bounty hunting scam joins two men in an uneasy
                     alliance against a third in a race to find a fortune in
                     gold buried in a remote cemetery.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=UHctLmLIrpQ',
        'imdb_rating': '8.9',
        'imdb_url': 'http://www.imdb.com/title/tt0060196'
    },
    {
        'title': 'Fight Club',
        'year': '1999',
        'storyline': """An insomniac office worker, looking for a way to
                     change his life, crosses paths with a devil-may-care
                     soapmaker, forming an underground fight club that evolves
                     into something much, much more.""",
        'image': 'https://ia.media-imdb.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg',  # NOQA
        'trailer': 'https://www.youtube.com/watch?v=SUXWAEX2jlg',
        'imdb_rating': '8.8',
        'imdb_url': 'http://www.imdb.com/title/tt0137523'
    }
]

# create a list of movies based on the params
movies = []
position = 0
for movie in movies_params:
    position += 1
    movie = media.Movie(movie['title'],
                        movie['storyline'],
                        movie['image'],
                        movie['trailer'],
                        position,
                        movie['year'],
                        movie['imdb_rating'],
                        movie['imdb_url'])
    movies.append(movie)

# open the html page with all the movies in the list
fresh_tomatoes.open_movies_page(movies)
