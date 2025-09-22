print("Simple Profile Maker")
print("Fill the fields and see the types.")

# Gathering data (string, int, float, int)
who = input("Name -> ")
ageCount = int(input("Age -> "))
m_height = float(input("Height in meters -> "))
magicNo = int(input("Favourite number -> "))

# Showing details
print("\nProfile Summary")
print("who:", who, "|", "Type:", type(who), "|", "Memory:", id(who))
print("ageCount:", ageCount, "|", "Type:", type(ageCount), "|", "Memory:", id(ageCount))
print("m_height:", m_height, "|", "Type:", type(m_height), "|", "Memory:", id(m_height))
print("magicNo:", magicNo, "|", "Type:", type(magicNo), "|", "Memory:", id(magicNo))

# Birth year using division/multiplication demo (simple arithmetic mixed in comments)
approx_year = 2025 - ageCount
print("\nApprox birth year:", approx_year, "(based on age).")
print("Bye!")