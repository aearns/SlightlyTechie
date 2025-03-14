
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    author VARCHAR(128) NOT NULL,
    year_published INT NOT NULL
);


INSERT INTO books (title, author, year_published)
VALUES
    ('The Beauty and the Beast', 'L. Reed', 1825),
    ('Ei, Ghanaman', 'Biibini', 2025),
    ('To Kill a Goat', 'Addo D', 1960),
    ('Pride and Injustice', 'Jane Mary', 1813),
    ('Things Fall Apart', 'Chinua Achebe', 1997);

SELECT * FROM books;