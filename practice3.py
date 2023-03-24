from typing import TypedDict

def mappings1(arg):  # change only this line
    arg = {1: 2, 3: 4}
    print(arg)


def mappings2(arg):  # change only this line
    arg = {"a": 1, "b": 2}
    print(arg)


def mappings3(arg):  # change only this line
    arg = {"a": [1], "b": [2]}
    print(arg)


def mappings4(arg):  # change only this line
    arg = None    
    arg = {1: 2, 3: 4, 5: "5"}
    print(arg)


def mappings5(arg):  # change only this line
    arg = {"test": [1], "test2": [2], 5: "5"}
    print(arg)


def mappings6(arg, arg2=None):  # change only this line
    arg = {"a": [1, 1.0], "b": [2]}
    arg2 = {"a": [1, None], "b": [2, "2"]}
    print(arg, arg2)


class Movie(TypedDict):
    # Fix this typed dict definition
    name: str


movie: Movie = {
    'name': 'Blade Runner',
    'year': 1982,
    'director': 'Ridley Scott',
    'genres': ['action', 'adventure'], 
    'alternative_titles': ['Blade Runner: Androids Dream'],
    'keywords': {1: 'blade', '2': 'Runner'}
}
