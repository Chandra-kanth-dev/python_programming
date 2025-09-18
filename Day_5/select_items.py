import os
from supabase import create_client, Client  # pip install supabase
from dotenv import load_dotenv  # pip install python-dotenv
load_dotenv()

url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def list_books():
    books = sb.table("books").select("*").execute()
    return books.data
def list_mems():
    mems = sb.table("members").select("*").execute() 
    return mems.data
#searh book with title/author/category
def search_books(query):
    results = sb.table("books").select("*").or_(
        f"title.ilike.%{query}%,author.ilike.%{query}%,category.ilike.%{query}%"
    ).execute()
    return results.data

#Show member details and their borrowed books.
def show_member_borrowed_books(member_id):
    results = sb.table("borrowed_books").select("*").eq("member_id", member_id).execute()
    return results.data
if __name__ == "__main__":
    choice = input("List books or members? (book/mem): ").strip().lower()
    if choice == "book":
        books = list_books()
        if books:
            print("Books:")
            for b in books:
                print(f"{b['id']}: {b['title']} by {b['author']} (Category: {b['category']}) — stock: {b['stock']}")
        else:
            print("No books found.")
        
        search_query = input("Enter search query (title/author/category) or press Enter to skip: ").strip()
        if search_query:
            search_results = search_books(search_query)
            if search_results:
                print("Search Results:")
                for b in search_results:
                    print(f"{b['id']}: {b['title']} by {b['author']} (Category: {b['category']}) — stock: {b['stock']}")
            else:
                print("No matching books found.")
                
    elif choice == "mem":
        mems = list_mems()
        if mems:
            print("Members:")
            for m in mems:
                print(f"{m['id']}: {m['name']} (Email: {m['email']})")
        else:
            print("No members found.")
        
        member_id = input("Enter member ID to view borrowed books or press Enter to skip: ").strip()
        if member_id.isdigit():
            borrowed_books = show_member_borrowed_books(int(member_id))
            if borrowed_books:
                print(f"Borrowed Books for Member ID {member_id}:")
                for bb in borrowed_books:
                    print(f"Book ID: {bb['book_id']}, Borrow Date: {bb['borrow_date']}, Return Date: {bb.get('return_date', 'Not returned')}")
            else:
                print("No borrowed books found for this member.")
    else:
        print("Invalid choice. Please enter 'book' or 'mem'.")
