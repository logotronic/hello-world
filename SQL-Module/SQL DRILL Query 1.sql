
SELECT BOOK.Title, BOOK.PublisherName,BOOK_COPIES.No_Of_Copies,LIBRARY_BRANCH.BranchName,LIBRARY_BRANCH.Address
FROM BOOK INNER JOIN BOOK_COPIES
	ON BOOK.BookID=BOOK_COPIES.BookID
FULL JOIN LIBRARY_BRANCH ON BOOK_COPIES.BranchID=LIBRARY_BRANCH.BranchID
WHERE LIBRARY_BRANCH.BranchName='Sharpstown'
AND BOOK.Title='The Lost Tribe'




