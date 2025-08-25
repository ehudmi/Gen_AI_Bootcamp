SELECT COUNT (*) FROM actors;

INSERT INTO actors (first_name,last_name)
VALUES ('John','Goodman');

-- ERROR:  null value in column "age" of relation "actors" violates not-null constraint
-- Failing row contains (8, John, Goodman, null, null). 
-- because the constraint is non-null for age - as well as for first name and last name - the record will not be added