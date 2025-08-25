from contact_manager import *

def run_tests():
    contacts = {}

    print("\n--- Test: Add Contacts ---")
    c1 = {
        "first_name": "Alice",
        "last_name": "Smith",
        "phone": "111-111-1111",
        "email": "alice@email.com",
        "address": {"street": "1 Main", "city": "Town", "state": "TX", "zip_code": "12345"},
        "category": "work",
        "notes": "",
        "created_date": today(),
        "last_modified": today()
    }
    add_contact(contacts, c1)

    c2 = {
        "first_name": "Bob",
        "last_name": "Brown",
        "phone": "222-222-2222",
        "email": "",
        "address": {"street": "", "city": "City", "state": "CA", "zip_code": ""},
        "category": "personal",
        "notes": "",
        "created_date": today(),
        "last_modified": today()
    }
    add_contact(contacts, c2)

    list_all(contacts)

    print("\n--- Test: Search by name ---")
    search_name(contacts, "Alice")

    print("\n--- Test: Search by category ---")
    search_category(contacts, "personal")

    print("\n--- Test: Find by phone ---")
    find_phone(contacts, "222-222-2222")

    print("\n--- Test: Update contact ---")
    for cid in contacts:
        update_contact(contacts, cid)
        break

    print("\n--- Test: Delete contact ---")
    for cid in list(contacts.keys()):
        delete_contact(contacts, cid)
        break

    print("\n--- Test: Stats ---")
    contact_stats(contacts)

    print("\n--- Test: Duplicates ---")
    add_contact(contacts, c1)
    add_contact(contacts, c1)
    find_duplicates(contacts)

    print("\n--- Test: Merge contacts ---")
    ids = list(contacts.keys())
    if len(ids) >= 2:
        merge_contacts(contacts, ids[0], ids[1])
        display_contact(contacts, ids[0])

if __name__ == "__main__":
    run_tests()
