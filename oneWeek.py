import ssl
import smtplib
import ReminderProgram

email_sender=ReminderProgram.email_sender
email_password =ReminderProgram.email_password

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_sender
em['subject'] = typeR
em.set_content('{} in the category, {} to history ve "{}" reminder with note'.format(
    ReminderProgram.reminder_option.get(), reminder_date_entry.get(), text_field.get('1.0','end')))

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_sender, em.as_string())