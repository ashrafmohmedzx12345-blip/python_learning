"""تمرين اليوم: حذف طالب من القاموس
لدينا:
المطلوب: اكتب دالة اسمها remove_student تستقبل قاموس الطلاب واسم الطالب.
إذا كان الطالب موجودًا، احذفه من القاموس.
إذا لم يكن موجودًا، أرجع "not found".
إذا تم الحذف، أرجع "deleted".
تلميح: استخدم in وdel.
أرسل محاولتك، وسأصححها معك خطوة خطوة دون عرض الحل مسبقًا. """



students = {
    "Ahmed": 85,
    "Mohamed": 90,
    "Ali": 75,
    "Omar": 60
}

def remove_student(name):
  if name in students:
    del students[name]
    return "deleted"
  else:
    return "not found"
x=remove_student('Al')
print(x)

    
print(students)