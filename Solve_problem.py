"""تمرين Python اليوم: تحديث درجات الطلاب
نكمل تدريبنا على القواميس والدوال، دون الانتقال لموضوع جديد قبل تثبيت الأساسيات.
لدينا:
students = {
    "Ahmed": 85,
    "Mohamed": 90,>
    "Ali": 75,
    "Omar": 60
}
المطلوب
اكتب دالة باسم update_grade تستقبل:
قاموس الطلاب.
اسم الطالب.
الدرجة الجديدة.
وتنفذ الآتي:
تتحقق من وجود الطالب.
إذا كان موجودًا، تحدّث درجته.
إذا لم يكن موجودًا، ترجع "not found".
مثال:
x = update_grade(students, "Ahmed", 95)
print(x)
الناتج المتوقع:
95"""


students = {
    "Ahmed": 85,
    "Mohamed": 90,
    "Ali": 75,
    "Omar": 60
}


def update_grade(students,name,grade):
  
  if name in students:
    students[name]=grade
    return students[name]
  else:
    return  "not found"
  
x=  update_grade(students,'Ahmed',94)
print(x)
#الداله لها تاثير علي الديكشينري في خارجها 
print(students)