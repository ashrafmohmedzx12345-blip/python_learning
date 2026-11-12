"""اكتب دالة باسم get_top_student:
تستقبل قاموس الطلاب.
تبحث عن أعلى درجة.
ترجع اسم الطالب صاحب أعلى درجة.
الناتج المتوقع:
تلميحات:
استخدم for.
استخدم متغيرًا لتخزين أعلى درجة.
استخدم متغيرًا لتخزين اسم صاحب أعلى درجة.
قارن الدرجات باستخدام if.
لا تستخدم max() الآن؛ أريدك أن تتدرب على بناء منطق المقارنة بنفسك.
أرسل محاولتك، وسنراجعها سطرًا سطرًا."""


students = {
    "Ahmed": 85,
    "Mohamed": 90,
    "Ali": 75,
    "Omar": 60,
    "Hassan": 95
}


def get_top_student(students):
  top_grade=0
  top_student=""
  for i in students:
    if students[i]>top_grade:
      top_grade=students[i]
      top_student=i
      
  return  top_student 
  
x=   get_top_student( students)
print(x)
    
  
  