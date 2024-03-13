from java.util import Properties
from javax.mail import Session, Message
from javax.mail.internet import InternetAddress, MimeMessage

# Cấu hình thông tin email
mail_from = "mail@abc.com.vn"
mail_to_list = ["minhhh@ssg.vn", "another_email@example.com"]
mail_host = "10.X.Y.Z"
mail_port = "25"
use_authentication = False

# Tạo đối tượng Properties để cấu hình
properties = Properties()
properties["mail.smtp.host"] = mail_host
properties["mail.smtp.port"] = mail_port

# Không sử dụng xác thực
if not use_authentication:
    properties["mail.smtp.auth"] = "false"

# Tạo đối tượng Session
session = Session.getDefaultInstance(properties)

# Tạo đối tượng Message
message = MimeMessage(session)
message.setFrom(InternetAddress(mail_from))

# Thêm nhiều người nhận
for recipient_email in mail_to_list:
    message.addRecipient(Message.RecipientType.TO, InternetAddress(recipient_email))

message.setSubject("Test Email from Jython")

# Nội dung HTML body
html_content = """

"""

message.setContent(html_content, "text/html; charset=utf-8")

# Gửi email
Transport = session.getTransport("smtp")
Transport.connect(mail_host, mail_port)
Transport.sendMessage(message, message.getAllRecipients())
Transport.close()

print("Email sent successfully.")
