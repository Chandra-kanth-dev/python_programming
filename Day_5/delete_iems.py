import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv


load_dotenv()

# Get Supabase URL and key from environment variables
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)


# Delete member only if they have no borrowed books
def delete_member(member_id):
    # Check if the member has borrowed books
    borrowed_books = sb.table("borrowed_books").select("id").eq("member_id", member_id).execute()

    if borrowed_books.data:
        return {"message": "Member has borrowed books, cannot delete."}

    # If no borrowed books, delete the member
    resp = sb.table("members").delete().eq("id", member_id).execute()
    return resp.data


# Delete book only if it is not borrowed
def delete_book(book_id):
    # Check if the book is borrowed by any members
    borrowed_books = sb.table("borrowed_books").select("id").eq("book_id", book_id).execute()

    if borrowed_books.data:
        return {"message": "Book is borrowed, cannot delete."}

    # If not borrowed, delete the book
    resp = sb.table("books").delete().eq("id", book_id).execute()
    return resp.data


# Main execution
if __name__ == "__main__":
    choice = input("Delete member or book? (member/book): ").strip().lower()

    if choice == "member":
        member_id = int(input("Enter member ID to delete: ").strip())
        result = delete_member(member_id)
        if isinstance(result, dict) and "message" in result:
            print(result["message"])
        else:
            print("Deleted member:", result)

    elif choice == "book":
        book_id = int(input("Enter book ID to delete: ").strip())
        result = delete_book(book_id)
        if isinstance(result, dict) and "message" in result:
            print(result["message"])
        else:
            print("Deleted book:", result)

    else:
        print("Invalid choice. Please enter 'member' or 'book'.")
