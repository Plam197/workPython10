# File Handling
# ไฟล์  การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write/append (w)/extend (x)/append (a)/read (r)
try :
    f_iot = open('iot04.txt', 'x', encoding='utf-8')
    f_iot.write('Hello...')
    f_iot.write('Hi...\n')
    f_iot.write('สวัสดี...\n')

    f_iot.close()
except FileExistsError :
    print('กรุณาเปลี่ยนชื่อไฟล์ใหม่ดพราะซ้ำ...')