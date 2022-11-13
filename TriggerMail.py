import os
import glob
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



class fileread():
    def readfile(self, path_dir):
        count = 0
        for path in os.listdir(path_dir):
            if os.path.isfile(os.path.join(path_dir, path)):
                count += 1
        print("Total number of files", count)

    def countline(self, path_dir):
        txt_file_list = glob.glob(path_dir + '*.txt')
        self.text_list = []
        for file in txt_file_list:
            with open(file, 'r') as f:
                r_text_list = f.readlines()
                self.text_list.append(r_text_list)

    def output(self):
        cwd = os.getcwd()
        filename = 'output1_' + datetime.datetime.now().strftime("%Y_%m_%d_%I_%M_%S_%p") + ".txt"
        main_path = os.path.join(cwd, filename)
        with open(main_path, 'w') as file:
            file.write(str(self.text_list))
            file.close()

    def mailtrigger(self):
        sender = 'shubhu0899@gmail.com'
        reciever = 'shubhu0899@gmail.com'

        msg = MIMEMultipart()
        msg['From'] = ''.format(sender)
        msg['To'] = ','.join(reciever)
        msg['Subject'] = "Hello, This mail is sent through python code"
        body = "Total no. of files : 9"
        msg.attach(MIMEText(body, 'plain'))
        filename = "output1_2022_09_08_10_24_49_PM.txt"
        attachment = open("C:/Users/ASUS/PycharmProjects/pythontutorial/output1_2022_09_08_10_24_49_PM.txt", "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, 'wukd nrxq cbht pavs')
        text = msg.as_string()
        s.sendmail(sender, reciever, text)
        s.quit()
        print('Mail Sent Successfully')

    def execute(self, path_dir):
        self.readfile(path_dir)
        self.countline(path_dir)
        self.output()
        self.mailtrigger()

mode = 'w'
path_dir = r'E:/'

op = fileread()
op.execute(path_dir)

