# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write/append (w)/extend (x)/append (a)/read (r)

f_iot = open('iot05.txt', 'a', encoding='utf-8')
f_iot.write('111')
f_iot.write('222...\n')
f_iot.write('33...\n')

f_iot.close()