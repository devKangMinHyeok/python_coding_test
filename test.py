students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]

print(sorted(students, key=lambda student: student[2], reverse=True))
# [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]