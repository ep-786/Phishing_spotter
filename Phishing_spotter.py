email = input('Insert email:')
suspicious_words = ['urgent', 'immediately', 'verify your information', 'click here', 'paste the link', 'account suspended']

email = email.lower()

suspicious_words_found = []

for words in suspicious_words:
    if words in email:
        suspicious_words_found.append(words)
                
risk_score = 0 

################################################################

email_address = input(
    '''\nDoes the senders address match the companies/person official address? Type Yes, No or Unsure.
    *Check previous emails with this person or check company website to confirm*
''')

email_address = email_address.lower() 

while email_address not in ['yes', 'no', 'unsure']:
    print('Please enter a valid choice.')
    email_address = input(
'''\nDoes the senders address match the companies/person official address? Type Yes, No or Unsure.
*Check previous emails with this person or check company website to confirm*
''')

    email_address = email_address.lower()

if email_address == 'yes':
        risk_score += 0
elif email_address == 'no':
        risk_score += 25
elif email_address == 'unsure':
        risk_score += 5
        
################################################################
    
sensitive_information = input('''\nDoes the email ask for you to provide sensitive information? Type Yes or No.
*This includes your passwords, address, bank details, verification codes. To see full list type 'Full list'*
''')

sensitive_information = sensitive_information.lower()

while sensitive_information not in ['yes', 'no']:
        
    if sensitive_information == 'full list':
        print('''address/parts of address
bank information/parts of bank card information
full name
passwords
verification codes
''')

    else:
                  
        print('Please enter a valid choice.')
    
    sensitive_information = input(
'''\nDoes the email ask for you to provide sensitive information? Type Yes or No.
    *This includes your passwords, address, bank details, verification codes. To see full list type 'Full list'*
''')

    sensitive_information = sensitive_information.lower()


if sensitive_information == 'yes':
        risk_score += 25
elif sensitive_information == 'no':
        risk_score += 0
    
################################################################
    
threats = input(
    '''\nWhen reading the email do you feel pressured/threatened to do something right away? Type Yes or No.
*Check if words like, 'urgent', 'immediately' or 'asap' being used? Also check if the email hint at a negative outcome if not done*
''')

threats = threats.lower()

while threats not in ['yes', 'no']:
    
    print ('Please enter a valid choice.')
    
    threats = input(
'''\nWhen reading the email do you feel pressured/threatened to do something right away? Type Yes or No.
    *Check if words like, 'urgent', 'immediately' or 'asap' being used? Also check if the email hint at a negative outcome if not done*
''')

    threats = threats.lower()


if threats == 'yes':
    risk_score += 25
elif threats == 'no':
    risk_score += 0
    
################################################################
    
links_attachments = input('''\nDoes the email contain any suspicious links/attachments? Type Yes, No or Unsure
*This includes links for pictures, videos or another website, if they say its the company website check if it matches the official company url*
''')

links_attachments = links_attachments.lower()

while links_attachments not in ['yes', 'no', 'unsure']:
    
    print ('Please enter a valid choice.')
    
    links_attachments = input(
'''\nDoes the email contain any suspicious links/attachments? Type Yes, No or Unsure
    *This includes links for pictures, videos or another website, if they say its the company website check if it matches the official company url*
''')

    links_attachments = links_attachments.lower()

if links_attachments == 'yes':
    risk_score += 15
elif links_attachments == 'no':
    risk_score += 0
elif links_attachments == 'unsure':
    risk_score += 5
    
################################################################

unexpected_email = input('''\nAre you expecting an email from the sender?
''')

unexpected_email = unexpected_email.lower()

while unexpected_email not in ['yes', 'no', 'unsure']:
    
    print ('Please enter a valid choice.')
    
    unexpected_email = input(
'''\nAre you expecting an email from the sender?
    ''')

    unexpected_email = unexpected_email.lower()

if unexpected_email == 'yes':
    risk_score += 0
elif unexpected_email == 'no':
    risk_score += 10
elif unexpected_email == 'unsure':
    risk_score += 2
    
################################################################


print('\nWhile filling out the questions you got a total of', risk_score, ' points. The final verdict is shown below:')

if risk_score < 30:
    print('Your email does not seem to be phishing. Make sure not to share personal information before confirming the sender.')
elif risk_score <= 70:
    print('Your email may be phishing. Make sure not to send personal information before confirming the sender.')
else:
    print('There is a high chance that this email is phishing. Make sure not to share personal information before confirming the sender.')

if suspicious_words_found:
    print ('\nYour email contained these suspicious statements', suspicious_words_found,'. These phrases can appear in legitimate emails too but are commonly used in phishing emails. Look out for these words next time!')
else: 
    print()
    
print('\nWARNING! This does not automatically prove whether an email/message is phishing or not. This is for learning purposes only.')