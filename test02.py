# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write/append (w)/extend (x)/append (a)/read (r)

f_iot = open('iot.txt', 'w', encoding='utf-8')
f_iot.write('Hello...')
f_iot.write('Hi...\n')
f_iot.write('สวัสดี...\n')

f_iot.close()