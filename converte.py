import json
from reportlab.pdfgen import canvas

with open('dados.json') as  dados:
    data = json.load(dados)


my_canvas = canvas.Canvas("teste.pdf")
my_canvas.drawString(100, 750,  "AttendanceId:  " + data['attendanceId'])
my_canvas.drawString(100, 735,  "status:  "+ str(data['status']))
my_canvas.drawString(100, 720,  "description:  "+ str(data['secondaryDescription']))
my_canvas.drawString(100, 705,  "SecondaryDescription:  "+ str(data['secondaryDescription']))
my_canvas.drawString(100, 690,  "linkImage:  "+ str(data['linkImage']))
my_canvas.drawString(100, 675,  "countUnreadMessages:  "+ str(data['countUnreadMessages']))
my_canvas.drawString(100, 660,  "hasTag:  "+ str(data['hasTag']))
my_canvas.drawString(100, 645,  "lastSeen:  "+ str(data['lastSeen']))


data_contact = data['contact']
my_canvas.drawString(100, 606,  "Contact:  "+ str(data_contact['id']))
my_canvas.drawString(100, 590,  "id:  "+ str(data_contact['id']))
my_canvas.drawString(100, 575,  "name:  "+ str(data_contact['name']))
my_canvas.drawString(100, 560,  "secondaryName:  "+ str(data_contact['secondaryName']))
my_canvas.drawString(100, 545,  "number:  "+ str(data_contact['number']))
my_canvas.drawString(100, 530,  "linkImage:  "+ str(data_contact['linkImage']))
my_canvas.drawString(100, 515,  "isMe:  "+ str(data_contact['isMe']))
my_canvas.drawString(100, 500,  "tags:  "+ str(data_contact['tags']))

data_lastMessage = data['lastMessage']
my_canvas.drawString(100, 470,  "lastMessage:")
my_canvas.drawString(100, 450,  "id:  "+ str(data_lastMessage['id']))
my_canvas.drawString(100, 430,  "text:  "+ str(data_lastMessage['text']))
data_sender = data_lastMessage['sender']
my_canvas.drawString(100, 410,  "Sender:")
my_canvas.drawString(100, 395,  "id:  "+ str(data_sender['id']))
my_canvas.drawString(100, 380,  "name:  "+ str(data_sender['name']))
my_canvas.drawString(100, 365,  "secondaryName:  "+ str(data_sender['secondaryName']))
my_canvas.drawString(100, 350,  "number:  "+ str(data_sender['number']))
my_canvas.drawString(100, 335,  "linkImage:  "+ str(data_sender['linkImage']))
my_canvas.drawString(100, 320,  "isMe:  "+ str(data_sender['isMe']))

my_canvas.save()