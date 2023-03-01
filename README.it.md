# MyAnimeList

MyAnimeList è una semplice applicazione da riga di comando che ti aiuta a tenere traccia degli anime, dei film e dei
manga che hai visto, stai guardando o hai intenzione di guardare. Ti consente di gestire la tua lista anime comodamente
dalla linea di comando.

## Funzionalità

- Elenca tutti gli anime nella tua lista
- Filtra la lista per genere, stato e valutazione
- Mostra le informazioni su un anime specifico
- Aggiungi nuovi anime alla tua lista
- Rimuovi anime dalla tua lista
- Aggiorna le informazioni sugli anime esistenti
- ...

## Utilizzo

- **List:** per elencare tutti gli anime nella tua lista
    - Opzioni:
        - **--genre [genere]:** per filtrare la tua lista per genere
        - **--status [stato]:** per filtrare la tua lista per stato
        - **--rating [formato]:** per filtrare la tua lista per valutazione
            - **formato:** "[< | <= | = | > | >=]rating"
    - **Esempio:**
        - ./myanimelist list --genre action --status watching --rating "<4"

- **Show [nome]:** per mostrare informazioni su un anime specifico nella tua lista
    - **Esempio:**
        - ./myanimelist show Attack on Titan

- **Add [name]:** per aggiungere un nuovo anime alla tua lista
    - Opzioni (tutti i parametri sono opzionali):
        - **--genre:** considerare l'argomento fornito come genere
    - **Esempio:**
        - ./myanimelist add Attack On Titan
        - ./myanimelist add --genre action

- **Remove [nome]:** per rimuovere un anime dalla tua lista
    - Options (all parameters are optional):
        - **--genre:** considerare l'argomento fornito come genere
    - **Esempio:**
        - ./myanimelist remove Attack on Titan
        - ./myanimelist remove --genre action

- **Update [nome]:** per aggiornare un anime nella tua lista
    - Opzioni (tutti i parametri sono opzionali, ma almeno un parametro deve essere fornito.):
        - **--type [tipo]:** un nuovo tipo
          - **type:** Anime (default), Manga, Film
        - **--name [nome]:** un nuovo nome
        - **--genre [genere]:** un nuovo genere
        - **--season [stagione]:** una nuova stagione
        - **--episode [episodio]:** un nuovo episodio
          -**--status [stato]:** un nuovo stato
        - **--rating [valutazione]:** una nuova valutazione
    - **Esempio:**
        - ./myanimelist update --type film

- **Watch [name] [numero di episodio (default=1)]:** per guardare l'anime (aumentando il numero di episodi)
    - **Esempio:**
        - ./myanimelist watch Attack On Titan 2

## Installazione

TODO

## Licenza

MyAnimeList è rilasciato sotto la Licenza MIT.