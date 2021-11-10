--Jacob Hopkins
--assignment 1 warmup query
--2/10/2019

SELECT DISTINCT au_lname AS Last_Name, au_fname AS First_Name		-- select first and last name and no duplicates
FROM authors														-- from authors
JOIN titleauthor ON authors.au_id=titleauthor.au_id					-- join titleauthor by authorIDs
JOIN titles ON titles.title_id=titleauthor.title_id					-- join titles by titleID
JOIN sales ON titleauthor.title_id=sales.title_id					-- join sales by titleID
WHERE sales.qty>=1 AND titles.advance<=15.50						-- where quantity is greater then one AND price of title doesnt exceed 15.50
ORDER BY au_lname DESC;												-- order by their last name in decending order	