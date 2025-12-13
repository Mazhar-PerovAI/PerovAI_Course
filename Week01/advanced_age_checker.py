def age_group(age):
    if age < 12:
        return "Child"
    elif age < 18:
        return "Teen"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

age = int(input("Enter age: "))
print(age_group(age))