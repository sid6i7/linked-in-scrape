import os

LOGIN_URL = "https://www.linkedin.com/login"
os.environ['EMAIL'] = "siddhantjain208@gmail.com"
os.environ['PASSWORD'] = "siddhant@JAIN23"

USERNAME_ELEMENT = ""
PASSWORD_ELEMENT = ""
LOGIN_BTN_ELEMENT = ""

# use only after login
JOB_SEARCH_BASE_URL = "https://www.linkedin.com/jobs/search/"
INTERNSHIP_FILTER = "&f_JT=I"
SW_COMPANIES_FILTER = "&f_I=6%2C4%2C96"

COMPANY_ELEMENT_CLASS = "artdeco-entity-lockup__content"
INCREMENT_FILTER = "&start="