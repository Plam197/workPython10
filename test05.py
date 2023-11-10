# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write/append (w)/extend (x)/append (a)/read (r)

f_iot = open('iot.txt', 'r', encoding='utf-8')

data = f_iot.read()

f_iot.close()
print(data)