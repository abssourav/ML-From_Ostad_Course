-- Assignment on module 4
-- Problem Description
-- Imagine you are working with a database for a movie rental company.
-- The database has a table named Movies with the following structure:


CREATE SCHEMA movie_rental_company;
USE movie_rental_company;


-- CREATE TABLE WHICH CALLED MOVIES
CREATE TABLE Movies(
	MovieID INT PRIMARY KEY,
	Title VARCHAR(100),
    Genre VARCHAR(100),
    ReleaseYear YEAR,
    Rating DECIMAL(3,1),
    BoxOfficeRevenue INT(50),
    Director VARCHAR(100)
);

ALTER TABLE Movies 
MODIFY COLUMN BoxOfficeRevenue BIGINT;

INSERT INTO	Movies VALUES 
(1, 'Inception', 'Sci-Fi', 2010, 8.8, 830000000, 'Christopher Nolan'),
(2, 'Titanic', 'Romance', 1997, 7.8, 2200000000, 'James Cameron'),
(3, 'The Godfather', 'Crime', 1972, 9.2, 134000000, 'Francis Ford Coppola'),
(4, 'Avatar', 'Sci-Fi', 2009, 7.9, 2840000000, 'James Cameron'),
(5, 'Interstellar', 'Sci-Fi', 2014, 8.6, 677000000, 'Christopher Nolan'),
(6, 'Parasite', 'Thriller', 2019, 8.6, 264000000, 'Bong Joon Ho'),
(7, 'The Dark Knight', 'Action', 2008, 9.0, 1000000000, 'Christopher Nolan'),
(8, 'Schindler\'s List', 'Drama', 1993, 9.0, 322000000, 'Steven Spielberg'),
(9, 'The Shawshank Redemption', 'Drama', 1994, 9.3, 28300000, 'Frank Darabont'),
(10, 'Pulp Fiction', 'Crime', 1994, 8.9, 213000000, 'Quentin Tarantino');


-- 1. Retrieve all information about movies directed by Christopher Nolan.
SELECT * FROM MOVIES
WHERE Director = 'Christopher Nolan';

-- 2. Find all distinct genres in the Movies table.
SELECT DISTINCT Genre from Movies;

-- 3. Display the top 5 highest-rated movies, sorted by their rating in descending order.
SELECT Title,Rating FROM Movies
ORDER BY Rating DESC LIMIT 5;

-- 4. List all movies released before the year 2000.
SELECT Title,ReleaseYear FROM Movies
WHERE ReleaseYear < 2000 ;

-- 5. Show the total number of movies in each genre.
SELECT Genre, COUNT(*) as TotalMovies
FROM Movies
GROUP BY Genre;

-- 6. Find the total revenue of all movies in the Sci-Fi genre.
SELECT SUM(BoxOfficeRevenue) as TotalRevenueSciFi
FROM Movies
WHERE Genre = 'Sci-Fi';

-- 7. Retrieve the titles of movies with a rating greater than 8.5 but less than 9.0.
SELECT Title,Rating FROM Movies
where 8.5 < Rating AND Rating < 9.0
ORDER BY Rating DESC;

-- 8. Display the names of all movies that have the word 'The' in their title.
SELECT Title FROM Movies
where Title LIKE '%THE%';

-- 9. Find the movie with the highest box office revenue.
SELECT * FROM Movies
ORDER BY BoxOfficeRevenue DESC
LIMIT 1;

-- 10. Retrieve the average rating of all movies released after the year 2000.
SELECT AVG(Rating) as AverageRating
FROM Movies 
where ReleaseYear > 2000;