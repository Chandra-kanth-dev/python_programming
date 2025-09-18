import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from the .env file
load_dotenv()

# Get Supabase URL and key from environment variables
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)


# Update book stock
def update_book_stock(book_id, stock):
    payload = {"stock": stock}  # Update stock value
    resp = sb.table("books").update(payload).eq("id", book_id).execute()  # Using "id" to find the book
    return resp.data

# Update member information
def update_member_info(member_id, new_email):
    payload = {"email": new_email}  # Update email value
    resp = sb.table("members").update(payload).eq("id", member_id).execute()  # Using "id" to find the member
    return resp.data


# Main execution
if __name__ == "__main__":
    choice = input("Update book stock or member info? (book/member): ").strip().lower()
    
    if choice == "book":
        book_id = int(input("Enter book ID to update stock: ").strip())
        new_stock = int(input("Enter new stock: ").strip())
        updated_book = update_book_stock(book_id, new_stock)
        print("Updated book:", updated_book)
    
    elif choice == "member":
        member_id = int(input("Enter member ID to update info: ").strip())
        new_email = input("Enter new email: ").strip()
        updated_member = update_member_info(member_id, new_email)
        print("Updated member:", updated_member)
    
    else:
        print("Invalid choice. Please enter 'book' or 'member'.")
