USE dbMovie
GO

SELECT BOOK.Title,BOOK_AUTHORS.AuthorName,LIBRARY_BRANCH.BranchName,BOOK_COPIES.No_Of_Copies
FROM BOOK INNER JOIN BOOK_AUTHORS ON BOOK.BookID=BOOK_AUTHORS.BookID
INNER JOIN BOOK_COPIES ON BOOK_AUTHORS.BookID=BOOK_COPIES.BookID
INNER JOIN LIBRARY_BRANCH ON BOOK_COPIES.BranchID=LIBRARY_BRANCH.BranchID
WHERE BOOK_AUTHORS.AuthorName='Stephen King'
AND LIBRARY_BRANCH.BranchName='Central'

