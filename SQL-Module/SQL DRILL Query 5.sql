DECLARE @Branch VARCHAR(50)
SET @Branch ='Gotham'

SELECT LIBRARY_BRANCH.BranchName,COUNT(BOOK_LOANS.BookID) AS 'Total Books Checked Out'
FROM LIBRARY_BRANCH INNER JOIN BOOK_LOANS ON LIBRARY_BRANCH.BranchID=BOOK_LOANS.BranchID
WHERE LIBRARY_BRANCH.BranchName=@Branch
GROUP BY LIBRARY_BRANCH.BranchName