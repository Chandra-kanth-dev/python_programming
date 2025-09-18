import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from the .env file
load_dotenv()

# Get Supabase URL and key from environment variables
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)


def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data

# Function to add a member
def add_mem(name, email):
    payload = {"name": name, "email": email}  # Corrected: Removed "type", added "email"
    resp = sb.table("members").insert(payload).execute()
    return resp.data

# Main execution
if __name__ == "__main__":
    choice = input("Add book or member? (book/mem): ").strip().lower()
    if choice == "book":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        category = input("Enter category: ").strip()
        stock = int(input("Enter stock: ").strip())
        created = add_book(title, author, category, stock)
        print("Inserted book:", created)
    elif choice == "mem":
        name = input("Enter member name: ").strip()
        email = input("Enter email: ").strip()
        created = add_mem(name, email)
        print("Inserted member:", created)
    else:
        print("Invalid choice. Please enter 'book' or 'mem'.")
