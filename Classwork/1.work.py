
students = []
num_students = 3 

for i in range(1, num_students + 1):
    print(f"ID: {i}")
    name = input("Name: ")
    python_score = float(input("Python Score: "))
    java_score = float(input("Java Score: "))
    db_score = float(input("Database Score: "))

    total = python_score + java_score + db_score
    average = total / 3

    students.append({
        "id": i,
        "name": name,
        "total": total,
        "average": round(average, 2)
    })

    print("-" * 34)
print(f"{'ID':<5} {'Name':<10} {'Total':<10} {'Average'}")
for s in students:
    print(f"{s['id']:<5} {s['name']:<10} {s['total']:<10} {s['average']}")