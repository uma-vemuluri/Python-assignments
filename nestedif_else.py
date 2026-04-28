'''A local library wants to automate its book borrowing system. 
The system needs to determine the borrowing period based on the book type and the
 borrower's status. The library has the following rules: books can be borrowed for
   7 days by regular members, 14 days by premium members, and 30 days by staff 
   members. Additionally, reference books can only be borrowed by staff members 
   for 3 days.

Tasks / Requirements
Create a Python function calculate_borrowing_period that takes two parameters:
 book_type and member_status.
Use elif and nested if statements to implement the library's borrowing rules.
The function should return the borrowing period in days.
Test the function with different combinations of book_type and member_status to
 ensure it works correctly.
Add error handling to handle invalid input values for book_type and member_status.'''

def calculate_borrowing_period(book_type, member_status):
    book_type = book_type.lower()
    member_status = member_status.lower()

    if member_status == "regular":
        if book_type == "regular":
            return 7
        elif book_type == "reference":
            return "Reference books can only be borrowed by staff members."
        else:
            return "Invalid book type."

    elif member_status == "premium":
        if book_type == "regular":
            return 14
        elif book_type == "reference":
            return "Reference books can only be borrowed by staff members."
        else:
            return "Invalid book type."

    elif member_status == "staff":
        if book_type == "regular":
            return 30
        elif book_type == "reference":
            return 3
        else:
            return "Invalid book type."

    else:
        return "Invalid member status."
# Example calls :
print(calculate_borrowing_period("regular", "regular"))
print(calculate_borrowing_period("reference", "staff"))
print(calculate_borrowing_period("regular", "premium"))
print(calculate_borrowing_period("comic", "regular"))
print(calculate_borrowing_period("regular", "guest"))   

