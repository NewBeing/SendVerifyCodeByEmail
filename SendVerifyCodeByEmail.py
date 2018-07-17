import smtplib
import email.mime.multipart
import email.mime.text
import time, datetime, re, random
def verifyemail(eml):
    #msg = ''
    s = ''
    if len(eml) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", eml) != None:
            
            ###########生成验证码：6位数字##########
            verify_code=[]    #用于将每次产生的单个验证码保存起来
            i=1
            while i <= 6:                    #while循环用来产生八个随机数                  
                num=random.randint(0,9)
                char=str(num)
                verify_code.append(char)         #将每次产生的单个验证码追加到列表中。
                i+=1
            s="".join(verify_code)     
            ############验证码生成完毕##############

            message = email.mime.multipart.MIMEMultipart()
            msgFrom = 'ToDo.Mylist@gmail.com@gmail.com' #从该邮箱发送
            msgTo = eml #发送到该邮箱
            smtpSever='smtp.gmail.com' # 163邮箱的smtp Sever地址
            #smtpPort = '25' #开放的端口--163
            smtpPort = '587'
            sqm='bupt_todomy'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
            message['from'] = msgFrom
            message['to'] = msgTo
            message['subject'] = 'TODOLIST: Please Verify Your Account '
            content = '''
            Welcome to TODOLIST, 
                You are using this account to login TODOLIST,
                verify code is '''
            content += s
            content += '''
            You are using the email for related operations on this platform, we need to quickly verify your email address!
            In order to keep your account secure, please do not arbitrarily disclose the verification code to others. 
            If it is not your own operation, please ignore it.


            TODOLIST TEAM@copyright
            todo_list@163.com
            Company: TODOLIST TEAM
            Address: Beijing University of Posts and Telecommunications

            '''
            #content = 'hello everyone'
            txt = email.mime.text.MIMEText(content)
            message.attach(txt)
            smtp = smtplib
            smtp = smtplib.SMTP()
            
            '''
            smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
            '''
            smtp.connect(smtpSever, smtpPort)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(msgFrom, sqm)
            smtp.sendmail(msgFrom, msgTo, str(message))
            smtp.quit()
            msg = '验证码已发送, 请及时查看邮件!'
        else:
            msg = '邮箱格式有误, 请检查后重试!'
    else:
        msg = '邮箱格式有误, 请检查后重试!'

    output = {
        'verify_code' : s,
        'msg' : msg,
    }
    return output


print (verifyemail('1058782869@qq.com'))
