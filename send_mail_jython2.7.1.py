import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin SMTP server
smtp_server = 'mail.com'
smtp_port = 25
from_ = "mail@gmail.com"
to_ = ['minhhh@gmail.com', 'abc@gmail.com']
subject_ = 'Canh bao job treo'
body_ = """
Cac job dang bi treo, ngay du lieu, so luong hien tai:
#PVCB.p_notify_job_lag
"""

# Tạo một thư mới
msg = MIMEMultipart()
msg['From'] = from_
msg['To'] = ', '.join(to_)
msg['Subject'] = subject_

# Nội dung của thư
msg.attach(MIMEText(body_, 'plain'))

# Kết nối đến SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)

# Gửi thư đi
server.sendmail(from_, to_, msg.as_string())

# Đóng kết nối
server.quit()
