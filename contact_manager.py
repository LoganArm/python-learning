import json
import datetime

def today():
    d = datetime.datetime.now()
    return str(d.year) + "/" + str(d.month) + "/" + str(d.day)

def new_id(contacts):
    return "contact_" + str(len(contacts) + 1)

def create_contact():
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    cat = input("Category (personal/work/family): ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zipc = input("Zip: ")
    if first == "" or last == "" or phone == "":
        print("Missing required info")
        return None
    d = today()
    return {
        "first_name": first,
        "last_name": last,
        "phone": phone,
        "email": email,
        "address": {"street": street, "city": city, "state": state, "zip_code": zipc},
        "category": cat if cat != "" else "personal",
        "notes": "",
        "created_date": d,
        "last_modified": d
    }

def add_contact(db, c):
    if c is None:
        return
    cid = new_id(db)
    db[cid] = c
    print("Added:", cid)

def display_contact(db, cid):
    if cid not in db:
        print("Not found")
        return
    c = db[cid]
    print("\nID:", cid)
    print("Name:", c["first_name"], c["last_name"])
    print("Phone:", c["phone"])
    print("Email:", c["email"])
    print("Category:", c["category"])
    a = c["address"]
    print("Address:", a["street"], a["city"], a["state"], a["zip_code"])
    print("Created:", c["created_date"], " Last modified:", c["last_modified"])

def list_all(db):
    if len(db) == 0:
        print("No contacts")
    for cid in db:
        c = db[cid]
        print(cid, c["first_name"], c["last_name"], c["phone"])

def search_name(db, term):
    for cid in db:
        c = db[cid]
        if term in c["first_name"] or term in c["last_name"]:
            display_contact(db, cid)

def search_category(db, cat):
    for cid in db:
        if db[cid]["category"] == cat:
            display_contact(db, cid)

def find_phone(db, phone):
    for cid in db:
        if db[cid]["phone"] == phone:
            display_contact(db, cid)

def update_contact(db, cid):
    if cid not in db:
        print("No such contact")
        return
    field = input("Field to update: ")
    value = input("New value: ")
    db[cid][field] = value
    db[cid]["last_modified"] = today()
    print("Updated", cid)

def delete_contact(db, cid):
    if cid in db:
        del db[cid]
        print("Deleted", cid)

def merge_contacts(db, cid1, cid2):
    if cid1 not in db or cid2 not in db:
        print("One or both IDs not found")
        return
    c1 = db[cid1]
    c2 = db[cid2]
    for field in ["first_name", "last_name", "phone", "email", "category", "notes"]:
        if c1[field] == "" and c2[field] != "":
            c1[field] = c2[field]
    for field in ["street", "city", "state", "zip_code"]:
        if c1["address"][field] == "" and c2["address"][field] != "":
            c1["address"][field] = c2["address"][field]
    if c2["created_date"] < c1["created_date"]:
        c1["created_date"] = c2["created_date"]
    c1["last_modified"] = today()
    del db[cid2]
    print("Merged", cid2, "into", cid1)

def save_contacts(db, filename):
    try:
        with open(filename, "w") as f:
            json.dump(db, f, indent=2)
        print("Saved to", filename)
    except:
        print("Save failed")

def load_contacts(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return {}

def contact_stats(db):
    print("\n--- Stats ---")
    print("Total contacts:", len(db))
    cat_counts = {}
    for cid in db:
        cat = db[cid]["category"]
        if cat not in cat_counts:
            cat_counts[cat] = 0
        cat_counts[cat] += 1
    print("By category:", cat_counts)
    no_email = 0
    for cid in db:
        if db[cid]["email"] == "":
            no_email += 1
    print("Without email:", no_email)

def find_duplicates(db):
    phones = {}
    emails = {}
    names = {}
    print("\n--- Duplicates ---")
    for cid in db:
        c = db[cid]
        ph = c["phone"]
        em = c["email"]
        nm = c["first_name"] + " " + c["last_name"]
        if ph not in phones:
            phones[ph] = []
        phones[ph].append(cid)
        if em not in emails:
            emails[em] = []
        emails[em].append(cid)
        if nm not in names:
            names[nm] = []
        names[nm].append(cid)
    print("Phone duplicates:")
    for ph in phones:
        if len(phones[ph]) > 1:
            print(ph, phones[ph])
    print("Email duplicates:")
    for em in emails:
        if len(emails[em]) > 1:
            print(em, emails[em])
    print("Name duplicates:")
    for nm in names:
        if len(names[nm]) > 1:
            print(nm, names[nm])

def main():
    contacts = {}
    filename = "contacts.json"
    while True:
        print("\n--- Contact Manager ---")
        print("1 Add")
        print("2 List all")
        print("3 View contact")
        print("4 Search by name")
        print("5 Search by category")
        print("6 Find by phone")
        print("7 Update contact")
        print("8 Delete contact")
        print("9 Save")
        print("10 Load")
        print("11 Stats")
        print("12 Find duplicates")
        print("13 Merge contacts")
        print("0 Exit")
        choice = input("Choose: ")
        if choice == "1":
            c = create_contact()
            add_contact(contacts, c)
        elif choice == "2":
            list_all(contacts)
        elif choice == "3":
            cid = input("ID: ")
            display_contact(contacts, cid)
        elif choice == "4":
            term = input("Name search: ")
            search_name(contacts, term)
        elif choice == "5":
            cat = input("Category: ")
            search_category(contacts, cat)
        elif choice == "6":
            ph = input("Phone: ")
            find_phone(contacts, ph)
        elif choice == "7":
            cid = input("ID: ")
            update_contact(contacts, cid)
        elif choice == "8":
            cid = input("ID: ")
            delete_contact(contacts, cid)
        elif choice == "9":
            save_contacts(contacts, filename)
        elif choice == "10":
            contacts = load_contacts(filename)
            print("Loaded", len(contacts), "contacts")
        elif choice == "11":
            contact_stats(contacts)
        elif choice == "12":
            find_duplicates(contacts)
        elif choice == "13":
            c1 = input("First contact ID: ")
            c2 = input("Second contact ID: ")
            merge_contacts(contacts, c1, c2)
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
