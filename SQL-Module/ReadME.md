Notes by Logan Boespflug
Read ME FILE for SQL-Module Folder:

1)First Run "Item Number 30-Table Create.sql"
  A) CREATES TABLES
    -BOOK
    -BOOK_AUTHORS
    -PUBLISHER
    -BOOK_COPIES
    -BOOK_LOANS
    -BORROWER
    -LIBRARY_BRANCH
    
2)Files with 'UPDATE' will populate the table
   A) UPDATES TABLES
     -BOOK Table UPDATE.sql
     -BOOK_AUTHORS UPDATE.sql
     -PUBLISHER UPDATE.sql
     -BOOK_COPIES UPDATE.sql
     -BOOK_LOANS UPDATE.sql
     -BORROWER UPDATE.sql
     -LIBRARY_BRANCH UPDATE.sql

3)Files with 'DRILL' refers to the Tech Acadmey assigned to complete the following:
  #1 How many copies of the book titled The Lost Tribe are owned by the library branch whose name
is"Sharpstown"?
  #2 How many copies of the book titled The Lost Tribe are owned by each library branch?

  #3 Retrieve the names of all borrowers who do not have any books checked out.
  #4  For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today,
retrieve the book title, the borrower's name, and the borrower's address.

  #5 For each library branch, retrieve the branch name and the total number of books loaned out from
that branch.

  #6 Retrieve the names, addresses, and number of books checked out for all borrowers who have more
than five books checked out.

  #7 For each book authored (or co-authored) by "Stephen King", retrieve the title and the number of
copies owned by the library branch whose name is "Central"

4) Stored Procedures were created for Queries #5 [Change Library Branch Name] and #6 [Change the Amount of Books Checked Out]

END OF FILE

    
