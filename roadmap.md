Créer des faux données depuis Python
------------------------------------

Dans le chemin `store/models.py`,

Ajouter une dictionnaire : 

```python
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
```

Lier les données à l'urls.py et afficher dans une vue (views.py)
----------------------------------------------------------------
Dans le chemin `store/urls.py`,

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.listing)
]
```

Créer une vue dans `store/views.py`




