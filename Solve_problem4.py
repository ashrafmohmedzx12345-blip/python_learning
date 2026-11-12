"""تستقبل قاموس الطلاب.
تبحث عن أقل درجة.
ترجع اسم الطالب صاحب أقل درجة.
الناتج المتوقع:
شروط التمرين
استخدم for.
استخدم if.
لا تستخدم min().
لا تفترض أن أقل درجة تساوي صفرًا؛ ابدأ بأول درجة في القاموس.
تلميح: استخدم أول مفتاح في القاموس للحصول على أول درجة.
أرسل محاولتك، وسنراجعها سطرًا سطرًا. """

students = {
    "Ahmed": 85,
    "Mohamed": 90,
    "Ali": 35,
    "Omar": 60,
    "Hassan": 95
}
def get_lowest_student(students):
  name=list(students.keys())
  min_grade=students[name[0]]
  for i in students:
    if students[i]<min_grade:
      min_grade=students[i]
  return i
x=  get_lowest_student(students)
print(x)