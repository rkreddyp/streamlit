#from appsmills.streamlit_apps 
from helpers import openai_helpers
import streamlit as st
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re
## 

at = """ these are the attack techniques for business email compromise - - Exploiting Trusted Relationships
    - To urge victims to take quick action on email requests, attackers make a concerted effort to exploit an existing trusted relationship. Exploitation can take many forms, such as a vendor requesting invoice payments, an executive requesting iTunes gift cards, or an [employee sharing new payroll direct deposit details](https://www.armorblox.com/blog/payroll-fraud-when-direct-deposits-go-rogue).
- Replicating Common Workflows
    - An organization and its employees execute an endless number of business workflows each day, many of which rely on automation, and many of which are conducted over email. The more times employees are exposed to these workflows, the quicker they execute tasks from muscle memory. BEC attacks [try to replicate these day-to-day workflows](https://www.armorblox.com/blog/security-as-social-engineering-phishing-campaigns-spoofing-locked-account-workflows) to get victims to act before they think.
- Compromised workflows include:
    - Emails requesting a password reset
    - Emails pretending to share files and spreadsheets
    - Emails from commonly used apps asking users to grant them access
- Suspicious Attachments
    - Suspicious attachments in email attacks are often associated with malware. However, attachments used in BEC attacks forego malware in exchange for fake invoices and other social engineering tactics that add to the conversation’s legitimacy. These attachments are lures designed to ensnare targets further.
- Socially Engineered Content and Subject Lines
    - BEC emails often rely on subject lines that convey urgency or familiarity and aim to induce quick action.
    - Common terms used in subject lines include:
        - Request
        - Overdue
        - Hello FirstName
        - Payments
        - Immediate Action
    - Email content often follows along the same vein of trickery, with manipulative language that pulls strings to make specific, seemingly innocent requests. Instead of using phishing links, BEC attackers use language as the payload.
- Leveraging Free Software
    - Attackers make use of freely available software to lend BEC scams an air of legitimacy and help emails sneak past security technologies that block known bad links and domains.
    - For example, attackers use SendGrid to create spoofed email addresses and Google Sites to stand up phishing pages.
    - [Google Forms](https://www.armorblox.com/blog/ok-google-build-me-a-phishing-campaign)
"""

bc = """ these are the categories of business email compromise - - CEO Fraud
    - Attackers impersonate the CEO or executive of a company. As the CEO, they request that an employee within the accounting or finance department transfer funds to an attacker-controlled account.
- Lawyer Impersonation
    - Attackers pose as a lawyer or legal representative, often over the phone or email. These attacks’ common targets are lower-level employees who may not have the knowledge or experience to question the validity of an urgent legal request.
- Data Theft
    - Data theft attacks typically target HR personnel to obtain personal information about a company’s CEO or other high-ranking executives. The attackers can then use the data in future attacks like CEO fraud.
- Email Account Compromise
    - In an [email account compromise](https://www.armorblox.com/solutions/email-account-compromise) attack, an employee’s email account is hacked and used to request payments from vendors. The money is then sent to attacker-controlled bank accounts.
- Vendor Email Compromise
    - Companies with foreign suppliers are common targets of [vendor email compromise](https://www.armorblox.com/blog/identity-theft-invoices-and-impersonation). Attackers pose as suppliers, request payment for a fake invoice, then transfer the money to a fraudulent account.

"""

rank = """
urgency, lack of detail, attachments, generic salutation, unusual requests, spelling and grammar.

"""

et = """

Hello,

We emailed you a little while to ask for your help resolving an issue with your  account. Your account is still temporarily limited because we haven't heard from you.
We noticed some unusual log in activity with your account. Please check that no one has logged in to your account without your permission.
To help us with this and to see what you can and can’t do with your account until the issue is resolved, log in to your account and go to the Resolution Center.
As always, if you need help or have any questions, feel free to contact us. We're always here to help.
Thank you for being our customer.
Support team.

"""

def display_text () :

    button_name = "Check email for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "


    email_txt = st.text_area("Paste the email you want to check in place of the sample email below and click the check email button (or click the button with the sample email to check out" , value=et, height=400 )
    tab_button=st.button(button_name , key = "1")
    if tab_button:
        
        #r = openai_helpers.response( bc )
        #r = openai_helpers.response( at )

        prompt = " .determine if the below email is a business email compromise,  tell me the reasons and give me a bullet list of ranks (from 1-5) it in these categories: " + rank + ", categorize it and tell me the attack technique as well - "

        email_txt = prompt + email_txt
        openai_helpers.get_write_response ( bc + "." + at + "." + email_txt)

    

st.subheader ('Check Emails for BEC Attacks')
           
display_text()

    
