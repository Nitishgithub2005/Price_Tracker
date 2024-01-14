import requests
from bs4 import BeautifulSoup as BS
from smtplib import SMTP
import ssl
import schedule
import time as tm
import emojis
def program():
    URL="https://www.flipkart.com/hp-m070-wired-mechanical-mouse/p/itm912db2650cb13?pid=ACCGRU8EASFTUYAW&lid=LSTACCGRU8EASFTUYAWPDX6A1&marketplace=FLIPKART&store=6bo%2Fai3%2F2ay&srno=b_1_2&otracker=pp_reco_You%2Bmight%2Bbe%2Binterested%2Bin_2_36.dealCard.OMU_cid%3AS_F_N_6bo_ai3_2ay__d_50-100__NONE_ALL%3Bnid%3A6bo_ai3_2ay_%3Bet%3AS%3Beid%3A6bo_ai3_2ay_%3Bmp%3AF%3Bct%3Ad%3Bat%3ADEFAULT%3B&otracker1=pp_reco_PINNED_productRecommendation%2FAugmentSelling_You%2Bmight%2Bbe%2Binterested%2Bin_BANNER_HORIZONTAL_dealCard_cc_2_NA_view-all&fm=search-autosuggest&iid=en_XC-RaoIgjQyDRJwbAvowyJc7Jf5AfWqQ-WSwWeRzRqFfx03h6BkoDspcks_l4v4NquEUGPM4oVTF8bVlRIQhUg%3D%3D&ppt=pp&ppn=pp&ssid=zdcdxntjkg0000001705208298579"
    def extract_price():
        page = requests.get(URL)
        soup = BS(page.content, "html.parser")
        price = float(soup.find(class_="_30jeq3 _16Jk6d").text.split()[0].replace("₹", "").replace(",",""))
        return price

    def notify():
        SMTP_SERVER = "smtp.gmail.com"
        PORT = 587
        EMAIL_ID1 = "nitishmaladakar@gmail.com"#sender mail id
        EMAIL_ID2 = "nitishmaladakar2005@gmail.com"#reciver mail id
        PASSWORD = "cosq gzpa vmoj wzlz"
        now_price=str(extract_price())
        try:
            server = SMTP(SMTP_SERVER, PORT)
            context = ssl.create_default_context()
            server.starttls(context=context)
            server.login(EMAIL_ID1, PASSWORD)

            subject = "BUY NOW!!!"
            body = f"Price has fallen,The new price is Rs.{now_price} ,\nGo buy it now. The link for the product is given below\n" + URL
            msg = f"Subject:{subject}\n\n{body}"

            server.sendmail(EMAIL_ID1, EMAIL_ID2, msg)
            server.quit()
        except Exception as e:
            print(f"Error is{e}")    

    AFFORDABLE_PRICE = 400

    if extract_price() <= AFFORDABLE_PRICE:
        notify()
      

schedule.every().day.at("11:05").do(program)
while(True):
    schedule.run_pending()#checks if there are any scheduled tasks that is to be executed. If there is any pending task it will excecute 
    tm.sleep(1) # pauses the loop for 1 second before checking for pending tasks again. This helps in avoiding unnecessary CPU usage and gives a short interval for the scheduled tasks to be checked.