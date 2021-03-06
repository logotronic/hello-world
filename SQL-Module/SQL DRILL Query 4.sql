Use dbMovie
GO

DECLARE @Today DATE
SET @Today =GETDATE()

SELECT BORROWER.CardNO, BOOK.Title, BORROWER.Name, BORROWER.[Address], BORROWER.Phone, BOOK_LOANS.DueDate
FROM BOOK INNER JOIN BOOK_LOANS ON BOOK.BookID=BOOK_LOANS.BookID
INNER JOIN BORROWER ON BOOK_LOANS.CardNO=BORROWER.CardNO
INNER JOIN LIBRARY_BRANCH AS LIB ON BOOK_LOANS.BranchID=LIB.BranchID
WHERE LIB.BranchName='Sharpstown'
AND BOOK_LOANS.DueDate<@Today
