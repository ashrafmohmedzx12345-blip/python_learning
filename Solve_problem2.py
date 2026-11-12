"""المطلوب
اكتب دالة اسمها calculate_average:
تستقبل قاموس الطلاب.
تجمع جميع الدرجات.
تحسب متوسط الدرجات.
ترجع المتوسط باستخدام return.
تلميحات:
استخدم for للمرور على الدرجات.
استخدم متغيرًا لتجميع الدرجات.
استخدم len() لمعرفة عدد الطلاب.
مثال: متوسط الدرجات في القاموس يساوي 77.5.
أرسل محاولتك، ولن أعرض الحل قبل أن تجرب بنفسك. 💪"""
students = {
    "Ahmed": 85,
    "Mohamed": 90,
    "Ali": 75,
    "Omar": 60
}

def calculate_average(students):
  name=students.keys();
  total_grade=0;
  count=0;
  for i in name:
    total_grade+=students[i]
    count+=1
  average=total_grade/count
    
  return average  
  
x=  calculate_average(students)
print(x)
  