# Metflix(the grand rip-off):

## Make the movies and series storing and planning/rating app.

- When the app Starts I should be able to select my user from the list of available ones.
- Once user is selected I am presented with the lists I have available to me.
- Once I open the list I see all the movies and series added to those lists.

## Once I select the movie, I should be able to:

- Rate,
- Mark as watched,
- Mark as not watched.

To avoid re-entering all the data into the DB by hand use mokaroo or any other random data generator to get test data to fill your DB with on every delete of DB.

## Database setup:

- Movies: Title, Release year, rating,
- Series: Title, Release year, Amount of seasons running, rating
- To watch lists: Name, Date when created
- User: Name, Surname

(--- the relationship and foreign key fields are not mentioned, as a part of the task to add them accordingly ---)

## Relationships:

- User - One To Many -  Series/Movies
- To watch list - Many To Many - Series/Movies