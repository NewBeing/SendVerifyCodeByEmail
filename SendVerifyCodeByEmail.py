
import smtplib
import email.mime.multipart
import email.mime.text
import time, datetime, re, random
def verifyemail(eml):
    msg = ''
    code = ''
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
            code="".join(verify_code)     
            ############验证码 => s 生成完毕##############

            message = email.mime.multipart.MIMEMultipart()
            msgFrom = 'example@126.com' #从该邮箱发送
            msgTo = eml #发送到该邮箱
            smtpSever='smtp.126.com' # 邮箱的smtp Sever地址
            smtpPort = '25'
            sqm='example'  # 在登录smtp时需要login中的密码应当使用 授权码 而非账户密码
            message['from'] = msgFrom
            message['to'] = msgTo
            message['subject'] = 'YouKnowBook: Please Verify Your Account '

            content = '''
            Welcome to YouKnowBook, 

            You are using this account to login YouKnowBook, we need to quickly verify your email address!   
            the verification code is :  '''
            content += code
            content += '''
            In order to keep your account secure, please do not arbitrarily disclose the verification code 
            to others. If it is not your own operation, please ignore it.


            YouKnowBook TEAM @copyright
            example@126.com
            '''
            txt = email.mime.text.MIMEText(content)
            message.attach(txt)
            
            try:
                smtp = smtplib.SMTP()
                '''
                smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
                '''
                smtp.connect(smtpSever, smtpPort)
                smtp.login(msgFrom, sqm)
                smtp.sendmail(msgFrom, msgTo, str(message))
                smtp.quit()
                msg = '验证码已发送, 请及时查看邮件!'
            except smtplib.SMTPException as e:
                msg = e

    output = {
        'verify_code' : code,
        'msg' : msg,
    }
    return output

print (verifyemail('example@163.com'))

