from django.db import models

# Create your models here.

ARTISTS = {
    'Eminem': {'name': 'Eminem'},
    'Selena Gomez': {'name': 'Selena Gomez'},
    'Ed Sheeran': {'name': 'Ed Sheeran'}
}

ALBUMS = [
    {
        'name': 'Lose Yourself', 
        'artists': [ARTISTS['Eminem']]
    },
    {
        'name': 'Let Somebody Go', 
        'artists': [ARTISTS['Selena Gomez']]
    },
    {
        'name': 'Perfect', 
        'artists': [ARTISTS['Ed Sheeran']]
    },
]
