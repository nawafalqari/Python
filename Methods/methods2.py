text = 'Hello guys and welcome to my text'

print('Count:', text.count('t')) # لحساب عدد تكرار حرف
print('find:', text.find('o')) # لإيجاد رقم حرف معين
print('lower:', text.lower()) #
print('upper:', text.upper()) #
print('Swapcase:', text.swapcase()) # تبديل كل حرف صغير الى كبير والعكس
print('Title:', text.title()) # جعل اول حرف من كل كلمة الى حرف كبير مثل العنوان
print('Strip:', text.strip()) # حذف الاشياء الغير لازمة
print('Replace:', text.replace('guys', 'boys')) # استبدال كلمة بكلمة اخرى
print('Startswith:', text.startswith('Hello')) # Output = True, تحقق اذا بدأت الجملة بشيء معين
print('Endswith:', text.endswith('code')) # Output = false, نفس اللي فوق
print('Isalpha', text.isalpha()) # Output = False, لأن المسافة ليست من الحروف
print('Isdigit:', text.isdigit()) # Output = False, لا يوجد حروف
print('Isalnum', text.isalnum()) # Output = False, ليست كل الكلمات احرف وارقام
