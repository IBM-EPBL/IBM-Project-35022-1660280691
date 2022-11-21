import smtplib 

def send_conf_mail(registered_user_mail):
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

    #Use TLS to add security 
        smtp.starttls() 

        #User Authentication 
        smtp.login(<your-email-here>,<your-password-here>)

        #Defining The Message 
        message = 'Subject: {}\n\n{}'.format("Registration Successful", 'Your account to access Cardio Care has been successfully created')

        #Sending the Email
        smtp.sendmail(<your-email-here>, registered_user_mail, message) 

        #Terminating the session 
        smtp.quit() 
        print ("Email sent successfully!") 

    except Exception as ex: 
        print("Something went wrong....",ex)