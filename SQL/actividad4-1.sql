SELECT CustomerId FROM Invoice WHERE InvoiceId = 12;
SELECT FirstName FROM Customer WHERE CustomerId = 2;
SELECT FirstName FROM Customer WHERE CustomerId = (SELECT CustomerId FROM Invoice WHERE InvoiceId = 12);
SELECT AlbumId FROM Album WHERE Title LIKE 'b%' COLLATE NOCASE;
SELECT name FROM Track WHERE AlbumId IN (SELECT AlbumId FROM Album WHERE Title LIKE 'b%' COLLATE NOCASE);
SELECT Name FROM Track  WHERE MediaTypeId = (SELECT MediaTypeId FROM MediaType WHERE Name='Protected AAC audio file');
