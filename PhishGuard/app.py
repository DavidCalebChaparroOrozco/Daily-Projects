# Importing necessary libraries
import re
from email.parser import Parser
from urllib.parse import urlparse

# List of keywords commonly associated with phishing emails
PHISHING_KEYWORDS = [
    "urgent", "verify", "update", "password", "account", "click", "here",
    "login", "confirm", "secure", "bank", "paypal"
]

# List of known phishing domains (this is just an example)
KNOWN_PHISHING_DOMAINS = [
    "phishingsite.com",
    "malicioussite.net",
    "example-phishing.com",
    "fraudulent-site.org",
    "fakebanking.net",
    "phishingpage.info",
    "secure-login.com",
    "account-update.com",
    "verifyaccount.co",
    "urgent-action.net"
]


# Check if the email content contains phishing keywords or links to known phishing domains.
def is_phishing_email(email_content):
    # Check for phishing keywords in the email subject or body
    for keyword in PHISHING_KEYWORDS:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_content, re.IGNORECASE):
            return True

    # Extract URLs from the email content and check against known phishing domains
    urls = re.findall(r'http[s]?://\S+', email_content)
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain in KNOWN_PHISHING_DOMAINS:
            return True
    
    return False

# Filter a list of emails, returning only those that are not flagged as phishing.
def filter_phishing_emails(email_list):
    non_phishing_emails = []
    for email_content in email_list:
        if not is_phishing_email(email_content):
            non_phishing_emails.append(email_content)
    return non_phishing_emails

# Example usage with Hotmail emails (this is just a mock example)
hotmail_emails = [
    "Subject: Urgent! Please verify your account.\nClick here to update your password: http://phishingsite.com/update",
    "Subject: Your account statement.\nView your statement at: http://securebank.com/statement",
    "Subject: Meeting reminder.\nPlease join the meeting using the link: http://meetingsite.com",
    "Subject: Important notice: Update your billing information.\nVisit: http://example-phishing.com/billing",
    "Subject: Congratulations! You've won a prize.\nClaim your prize here: http://fraudulent-site.org/prize",
    "Subject: Account alert: Unusual login attempt detected.\nSecure your account: http://fakebanking.net/security",
    "Subject: Password reset requested.\nReset your password here: http://phishingpage.info/reset",
    "Subject: New login from unknown device.\nVerify your identity: http://secure-login.com/verify",
    "Subject: Your order has been shipped.\nTrack your order here: http://legitshop.com/track",
    "Subject: Weekly newsletter.\nRead more: http://newslettersite.com/weekly",
    "Subject: Update your account information.\nVisit: http://account-update.com/update",
    "Subject: Verify your email address.\nClick here: http://verifyaccount.co/email",
    "Subject: Important security update.\nMore info: http://urgent-action.net/security",
    "Subject: Welcome to our service!\nGet started: http://welcome.com/start",
    "Subject: Your subscription has been renewed.\nDetails: http://subscription.com/details",
    "Subject: Invoice for your recent purchase.\nView invoice: http://legitshop.com/invoice",
    "Subject: Please review your recent activity.\nSee activity: http://activityreview.com/details",
    "Subject: Security alert: Unauthorized access attempt.\nSecure your account: http://phishingsite.com/secure",
    "Subject: Action required: Update your payment method.\nUpdate here: http://updatepayment.com",
    "Subject: Your flight itinerary.\nCheck itinerary: http://airlinesite.com/itinerary",
    "Subject: Payment receipt.\nView receipt: http://paymentsite.com/receipt",
    "Subject: Reminder: Upcoming event.\nEvent details: http://eventsite.com/details",
    "Subject: Your weekly digest.\nRead digest: http://digestsite.com/weekly",
    "Subject: Please verify your account information.\nVerify now: http://phishingsite.com/verify",
    "Subject: Your package is out for delivery.\nTrack package: http://deliverysite.com/track"
]


# Filter out phishing emails
safe_emails = filter_phishing_emails(hotmail_emails)

# Print out the safe emails
for email in safe_emails:
    print("Safe Email:\n", email)
