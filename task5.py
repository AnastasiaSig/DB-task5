from pprint import pprint

import sqlalchemy

dsn = 'postgresql://Anastasia:Anastasia@localhost:5432/task_3'
engine = sqlalchemy.create_engine(dsn)

connection = engine.connect()

pprint(connection.execute('''SELECT g.name, COUNT(ArtistID) from ArtistGenre ag
LEFT JOIN Genres g ON ag.GenreId = g.Id
GROUP BY g.name;
''').fetchall())

pprint(connection.execute('''SELECT a.name, a.year, COUNT(t.ID) from Tracks t
LEFT JOIN Albums a ON t.AlbumId = a.Id
WHERE a.year = 2019 OR a.year = 2020
GROUP BY a.name, a.year;
''').fetchall())

pprint(connection.execute('''SELECT a.name, AVG(Lenght) from Tracks t
LEFT JOIN Albums a ON t.AlbumId = a.Id
GROUP BY a.name;
''').fetchall())

pprint(connection.execute('''SELECT ar.name from Artists ar
JOIN ArtistAlbum aa ON ar.Id = aa.ArtistId
JOIN Albums al ON aa.AlbumId = al.Id
WHERE al.year != 2020
GROUP BY ar.name;
''').fetchall())

pprint(connection.execute('''SELECT ar.name, c.name from Collections c
# LEFT JOIN TrackCollection tc ON c.Id = tc.CollectionId
# LEFT JOIN Tracks t ON tc.TrackId = t.Id
# JOIN Albums al ON al.Id = t.AlbumId
# LEFT JOIN ArtistAlbum aa ON al.Id = aa.albumId
# LEFT JOIN Artists ar ON aa.artistId = ar.Id
# WHERE ar.name = 'Milky Chance'
# GROUP BY ar.name, c.name;
# ''').fetchall())

pprint(connection.execute('''SELECT al.name, COUNT(ag.GenreId) from ArtistGenre ag
LEFT JOIN Artists ar ON ag.ArtistId = ar.Id
LEFT JOIN ArtistAlbum aa ON ar.Id = aa.ArtistId
LEFT JOIN Albums al ON aa.AlbumId = al.Id
GROUP BY al.name
HAVING COUNT(ag.GenreId) > 1;
''').fetchall())

pprint(connection.execute('''SELECT t.name from Tracks t
LEFT JOIN TrackCollection tc ON t.Id = tc.TrackId
GROUP BY t.name
HAVING COUNT(tc.TrackId) < 1;
''').fetchall())

pprint(connection.execute('''SELECT ar.name, t.name, t.lenght from Tracks t
LEFT JOIN Albums al ON t.AlbumId = al.Id
LEFT JOIN ArtistAlbum aa ON al.Id = aa.AlbumId
LEFT JOIN Artists ar ON aa.ArtistId = ar.Id
WHERE t.lenght = (
    SELECT MIN(lenght) FROM Tracks)
GROUP BY ar.name, t.name, t.lenght;
''').fetchall())

pprint(connection.execute('''SELECT al.name, MIN(COUNT(t.AlbumId)) OVER() from Tracks t
LEFT JOIN Albums al ON t.AlbumId = al.Id
GROUP BY al.name
''').fetchall())