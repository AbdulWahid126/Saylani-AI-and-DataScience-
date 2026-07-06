import streamlit as st
from library_system import Library

# Initialize the library in session state so it persists
if 'library' not in st.session_state:
    st.session_state.library = Library()
    # Adding some initial data
    st.session_state.library.add_book("B001", "Python Crash Course", "Eric Matthes", 5)
    st.session_state.library.add_book("B002", "Clean Code", "Robert C. Martin", 3)
    st.session_state.library.add_book("B003", "Design Patterns", "Erich Gamma", 2)
    st.session_state.library.add_user("U001", "Alice Smith")
    st.session_state.library.add_user("U002", "Bob Jones")

lib = st.session_state.library

st.set_page_config(page_title="Digital Library", page_icon="📚", layout="wide")

st.title("📚 Digital Library Management System")

# Sidebar for navigation
menu = ["View All Books", "Add New Book", "Search Book", "Borrow Book", "Return Book", "Check Availability", "Manage Users"]
choice = st.sidebar.selectbox("Navigation Menu", menu)

if choice == "View All Books":
    st.header("All Books in Library")
    books = lib.view_all_books()
    if books:
        for book in books:
            st.write(f"**{book.title}** by {book.author}")
            st.text(f"ID: {book.book_id} | Total: {book.total_copies} | Available: {book.available_copies}")
            st.divider()
    else:
        st.info("No books available in the library.")

elif choice == "Add New Book":
    st.header("Add a New Book")
    with st.form("add_book_form"):
        book_id = st.text_input("Book ID")
        title = st.text_input("Title")
        author = st.text_input("Author")
        copies = st.number_input("Total Copies", min_value=1, step=1)
        submit = st.form_submit_button("Add Book")

        if submit:
            if book_id and title and author:
                success, msg = lib.add_book(book_id, title, author, int(copies))
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please fill in all fields.")

elif choice == "Search Book":
    st.header("Search for a Book")
    search_type = st.radio("Search By", ["Title", "Author"])
    query = st.text_input(f"Enter {search_type}")
    
    if st.button("Search"):
        if query:
            if search_type == "Title":
                results = lib.search_by_title(query)
            else:
                results = lib.search_by_author(query)
                
            if results:
                st.success(f"Found {len(results)} matching book(s):")
                for book in results:
                    st.write(f"- **{book.title}** by {book.author} (ID: {book.book_id}) - Available: {book.available_copies}/{book.total_copies}")
            else:
                st.warning("No books found matching your query.")
        else:
            st.error("Please enter a search term.")

elif choice == "Borrow Book":
    st.header("Borrow a Book")
    with st.form("borrow_form"):
        user_id = st.text_input("User ID")
        book_id = st.text_input("Book ID")
        submit = st.form_submit_button("Borrow")
        
        if submit:
            if user_id and book_id:
                success, msg = lib.borrow_book(user_id, book_id)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please provide both User ID and Book ID.")

elif choice == "Return Book":
    st.header("Return a Book")
    with st.form("return_form"):
        user_id = st.text_input("User ID")
        book_id = st.text_input("Book ID")
        submit = st.form_submit_button("Return")
        
        if submit:
            if user_id and book_id:
                success, msg = lib.return_book(user_id, book_id)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please provide both User ID and Book ID.")

elif choice == "Check Availability":
    st.header("Check Book Availability")
    book_id = st.text_input("Enter Book ID")
    if st.button("Check"):
        if book_id:
            found, msg = lib.check_availability(book_id)
            if found:
                st.success(msg)
            else:
                st.error(msg)
        else:
            st.warning("Please enter a Book ID.")

elif choice == "Manage Users":
    st.header("Manage Users")
    st.subheader("Add New User")
    with st.form("add_user_form"):
        user_id = st.text_input("User ID")
        name = st.text_input("User Name")
        submit = st.form_submit_button("Register User")
        if submit:
            if user_id and name:
                success, msg = lib.add_user(user_id, name)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please fill in all fields.")
                
    st.subheader("All Registered Users")
    if lib.users:
        for u in lib.users.values():
            st.write(f"- **{u.name}** (ID: {u.user_id}) - Borrowed Books: {', '.join(u.borrowed_books) if u.borrowed_books else 'None'}")
    else:
        st.info("No users registered.")
