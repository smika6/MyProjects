--Jacob Hopkins
--generate 3 sets of 10 characters
--insert random lowercase letters into these sets
--do UNION INTERSECT and EXCEPT select operations on these sets

CREATE TEMPORARY TABLE setA (
	a CHAR() NOT NULL,
	b CHAR() NOT NULL,
	c CHAR() NOT NULL,
	d CHAR() NOT NULL,
	e CHAR() NOT NULL,
	f CHAR() NOT NULL,
	g CHAR() NOT NULL,
	h CHAR() NOT NULL,
	i CHAR() NOT NULL,
	j CHAR() NOT NULL
);

CREATE TEMPORARY TABLE setB (
	a CHAR() NOT NULL,
	b CHAR() NOT NULL,
	c CHAR() NOT NULL,
	d CHAR() NOT NULL,
	e CHAR() NOT NULL,
	f CHAR() NOT NULL,
	g CHAR() NOT NULL,
	h CHAR() NOT NULL,
	i CHAR() NOT NULL,
	j CHAR() NOT NULL
);

CREATE TEMPORARY TABLE setC (
	a CHAR() NOT NULL,
	b CHAR() NOT NULL,
	c CHAR() NOT NULL,
	d CHAR() NOT NULL,
	e CHAR() NOT NULL,
	f CHAR() NOT NULL,
	g CHAR() NOT NULL,
	h CHAR() NOT NULL,
	i CHAR() NOT NULL,
	j CHAR() NOT NULL
);
INSERT INTO setA
	(a,b,c,d,e,f,g,h,i,j)
	VALUES (CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97));
	
INSERT INTO setB
	(a,b,c,d,e,f,g,h,i,j)
	VALUES (CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97));
	
INSERT INTO setC
	(a,b,c,d,e,f,g,h,i,j)
	VALUES (CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97),
	CHAR(abs(random()%(123-97))+97),CHAR(abs(random()%(123-97))+97));

	
	
SELECT "";
SELECT "Displaying sets";
SELECT * FROM setA;
SELECT * FROM setB;
SELECT * FROM setC;
SELECT "";
SELECT "";



SELECT "UNION";
SELECT DISTINCT * FROM setA 
UNION 
SELECT DISTINCT * FROM setB;
SELECT "";

SELECT DISTINCT * FROM setA
UNION
SELECT DISTINCT * FROM setC;
SELECT "";

SELECT DISTINCT * FROM setB
UNION
SELECT DISTINCT * FROM setC;
SELECT "";
SELECT "";



SELECT "INTERSECT";
SELECT DISTINCT * FROM setA
INTERSECT
SELECT DISTINCT * FROM setB;
SELECT "";

SELECT DISTINCT * FROM setA
INTERSECT
SELECT DISTINCT * FROM setC;
SELECT "";

SELECT DISTINCT * FROM setB
INTERSECT
SELECT DISTINCT * FROM setC;
SELECT "";
SELECT "";




SELECT "EXCEPT";
SELECT DISTINCT * FROM setA
EXCEPT
SELECT DISTINCT * FROM setB;
SELECT "";

SELECT DISTINCT * FROM setA
EXCEPT
SELECT DISTINCT * FROM setC;
SELECT "";

SELECT DISTINCT * FROM setB
EXCEPT
SELECT DISTINCT * FROM setC;
SELECT "";
SELECT "";