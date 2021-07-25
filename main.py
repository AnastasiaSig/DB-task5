from pprint import pprint

import sqlalchemy

dsn = 'postgresql://Anastasia:Anastasia@localhost:5432/task_3'
engine = sqlalchemy.create_engine(dsn)

connection = engine.connect()

pprint(sqlalchemy.inspect(engine).get_table_names())

connection.execute('''INSERT INTO Genres(Name)
            VALUES('rock');
''')

connection.execute('''INSERT INTO Genres(Name)
            VALUES
                ('pop'),
                ('indie'),
                ('hip hop'),
                ('electro');
''')

connection.execute('''INSERT INTO artists(Name)
             VALUES
                 ('AC/DC'),
                 ('Ozzy Osbourne'),
                 ('Pink'),
                 ('Lady Gaga'),
                 ('Milky Chance'),
                 ('Sonic Youth'),
                 ('Kaney West'),
                 ('Gorillaz'),
                 ('Justice'),
                 ('Daft Punk');
 ''')

connection.execute('''INSERT INTO albums(Name, Year)
             VALUES
                 ('POWER UP', 2020),
                 ('Rock or Bust', 2014),
                 ('Ordinary Man', 2020),
                 ('Under Cover', 2005),
                 ('Hurts 2B Human', 2019),
                 ('Beautiful Trauma', 2017),
                 ('Chromatica', 2020),
                 ('Joanne', 2016),
                 ('Mind the Moon', 2019),
                 ('Blossom', 2017),
                 ('Spinhead Sessions', 2016),
                 ('The Eternal', 2009),
                 ('KIDS SEE GHOSTS', 2018),
                 ('ye', 2018),
                 ('The Now Now', 2018),
                 ('The Fall', 2010),
                 ('Escapades', 2021),
                 ('Woman Worldwide', 2018),
                 ('Random Access Memory', 2013),
                 ('Human After All', 2005);
 ''')

connection.execute('''INSERT INTO tracks(Name, Lenght, AlbumId)
             VALUES
                 ('Realize', 3.38, 1),
                 ('Shot in the Dark', 3.05, 1),
                 ('Hard Times', 2.45, 2),
                 ('Rock or Bust', 3.04, 2),
                 ('Ordinary Man', 5.03, 3),
                 ('All My Life', 4.18, 3),
                 ('In My Life', 3.30, 4),
                 ('Woman', 3.46, 4),
                 ('Hustle', 2.56, 5),
                 ('My Attic', 3.03, 5),
                 ('What about us', 4.30, 6),
                 ('For Now', 3.37, 6),
                 ('Alice', 2.58, 7),
                 ('Rain On Me', 3.02, 7),
                 ('Million Reasons', 3.25, 8),
                 ('Angel Down', 3.50, 8),
                 ('Fado', 4.10, 9),
                 ('The Game', 3.33, 9),
                 ('Blossom', 4.13, 10),
                 ('Ego', 3.52, 10),
                 ('Theme With Noise', 4.16, 11),
                 ('High Mesa', 8.37, 11),
                 ('Antenna', 6.13, 12),
                 ('No Way', 3.52, 12),
                 ('Fire', 2.20, 13),
                 ('Reborn', 5.25, 13),
                 ('Yikes', 3.09, 14),
                 ('All Mine', 2.25, 14),
                 ('Tranz', 2.43, 15),
                 ('Kansas', 4.08, 15),
                 ('Revolving Doors', 3.26, 16),
                 ('Hillbilly Man', 3.50, 16),
                 ('Welcome', 0.38, 17),
                 ('Captain', 3.22, 17),
                 ('Safe and Sound', 7.32, 18),
                 ('Dance', 3.16, 18),
                 ('Get Lucky', 6.10, 19),
                 ('Within', 3.48, 19),
                 ('Human After All', 5.20, 20),
                 ('Rock Robot', 4.48, 20);
 ''')

connection.execute('''INSERT INTO collections(Name, Year)
             VALUES
                 ('AC/DC collection', 2020),
                 ('Ozzy Osbourne collection', 2020),
                 ('Pink collection', 2019),
                 ('Lady Gaga collection', 2020),
                 ('Milky Chance collection', 2019),
                 ('Sonic Youth collection', 2016),
                 ('Kaney West collection', 2018),
                 ('Gorillaz collection', 2018),
                 ('Justice collection', 2021),
                 ('Daft Punk collection', 2015);
 ''')

connection.execute('''INSERT INTO ArtistGenre(ArtistId, GenreId)
             VALUES
                 (1, 1),
                 (2, 1),
                 (3, 3),
                 (4, 3),
                 (5, 4),
                 (6, 4),
                 (7, 5),
                 (8, 5),
                 (9, 6),
                 (10, 6);
 ''')

connection.execute('''INSERT INTO ArtistAlbum(ArtistId, AlbumId)
             VALUES
                 (1, 1),
                 (1, 2),
                 (2, 3),
                 (2, 4),
                 (3, 5),
                 (3, 6),
                 (4, 7),
                 (4, 8),
                 (5, 9),
                 (5, 10),
                 (6, 11),
                 (6, 12),
                 (7, 13),
                 (7, 14),
                 (8, 15),
                 (8, 16),
                 (9, 17),
                 (9, 18),
                 (10, 19),
                 (10, 20);
 ''')

connection.execute('''INSERT INTO TrackCollection(TrackId, CollectionId)
             VALUES
                 (1, 1),
                 (2, 1),
                 (3, 1),
                 (4, 1),
                 (5, 2),
                 (6, 2),
                 (7, 2),
                 (8, 2),
                 (9, 3),
                 (10, 3),
                 (11, 3),
                 (12, 3),
                 (13, 4),
                 (14, 4),
                 (15, 4),
                 (16, 4),
                 (17, 5),
                 (18, 5),
                 (19, 5),
                 (20, 5),
                 (21, 6),
                 (22, 6),
                 (23, 6),
                 (24, 6),
                 (25, 7),
                 (26, 7),
                 (27, 7),
                 (28, 7),
                 (29, 8),
                 (30, 8),
                 (31, 8),
                 (32, 8),
                 (33, 9),
                 (34, 9),
                 (35, 9),
                 (36, 9),
                 (37, 10),
                 (38, 10),
                 (39, 10),
                 (40, 10);
 ''')

connection.execute('''INSERT INTO ArtistGenre(ArtistId, GenreId)
             VALUES
                 (3, 1),
                 (8, 1);
 ''')

connection.execute('''INSERT INTO tracks(Name, Lenght, AlbumId)
             VALUES
                 ('Goodbye', 4.12, 3),
                 ('Joanne', 3.48, 8),
                 ('Cudi Montage', 3.23, 13);
 ''')