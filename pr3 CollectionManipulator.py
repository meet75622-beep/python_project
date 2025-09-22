bag = []  # list of student dicts

while True:
    print("\n1.Add  2.Show  3.Update  4.Delete  5.Subjects  6.Exit")
    op = input("Choose: ")

    if op == "1":
        roll = int(input("Student ID: "))
        nm = input("Name: ")
        ag = int(input("Age: "))
        gr = input("Grade: ")
        dob = input("DOB (YYYY-MM-DD): ")
        subj = input("Subjects (comma,comma): ")
        lock = (roll, dob)   # tuple immutable
        subs = list(set([p.strip() for p in subj.split(",") if p.strip()]))
        item = {"lock": lock, "name": nm, "age": ag, "grade": gr, "subjects": subs}
        bag.append(item)
        print("Saved.")
    elif op == "2":
        print("\n-- All Students --")
        if not bag:
            print("Empty.")
        else:
            for it in bag:
                rid, rdb = it["lock"]
                # old school % formatting
                print("ID: %s | Name: %s | Age: %s | Grade: %s | DOB: %s | Subjects: %s" % (
                    rid, it["name"], it["age"], it["grade"], rdb, ", ".join(it["subjects"])) )
    elif op == "3":
        who = int(input("ID to change: "))
        got = False
        for it in bag:
            if it["lock"][0] == who:
                got = True
                print("1.Age  2.Subjects")
                s = input("Field: ")
                if s == "1":
                    it["age"] = int(input("New age: "))
                elif s == "2":
                    it["subjects"] = list(set([x.strip() for x in input("New subjects: ").split(",") if x.strip()]))
                print("Updated.")
                break
        if not got:
            print("Not found.")
    elif op == "4":
        who2 = int(input("ID to remove: "))
        take = -1
        for i in range(len(bag)):
            if bag[i]["lock"][0] == who2:
                take = i
                break
        if take >= 0:
            del bag[take]
            print("Removed.")
        else:
            print("ID missing.")
    elif op == "5":
        box = set()
        for it in bag:
            box.update(it["subjects"])
        print("Subjects:", ", ".join(sorted(box)) if box else "None")
    elif op == "6":
        print("Bye!")
        break
    else:
        print("Try again.")
