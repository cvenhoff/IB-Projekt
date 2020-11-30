import wbdriver
import follow
import like
import comment
import direct_messaging
import search_acc_hashtag
import get_acc_pictures
import time
import follow
import unfollow
import profiledata
import userdata
from selenium.webdriver.support.ui import WebDriverWait

#driver
driver = wbdriver.driver
#parameters
comments_per_acc = 2
ppa = 4
pic_interval = 20
acc_interval = 30

def promo_func(hashtags, comments, interaction_number, job_list, pg_wg, pg_var, progressbar_wg):
    progressbar_wg['maximum'] = interaction_number
    #pg set functions
    pg_wg
    ref = interaction_number
    def set_pg_value(pg_value):
        pg_var.set(pg_value)
    def set_pg_text(tx):
        pg_wg.config(text=tx)
    #unfollow
    if(job_list[2]):
        set_pg_text("unfollowing accounts not following you")
        #unfollow not following accounts
        profiledata.collect_fol_data()
        unfollow.unfollow_func()
    #get accounts
    set_pg_text("searching for accounts")
    accounts = search_acc_hashtag.search(hashtags, interaction_number, ppa, job_list)
    #interact with every account
    for acc in accounts:
        #return if interrupted
        if(userdata.promo_running_flag == False):
            return
        set_pg_text("interacting with: " + (acc.split("/"))[3])
        if(interaction_number > 0):
            global comments_per_acc
            comment_counter = comments_per_acc
            #get to account
            driver.get(acc)
            if(job_list[0] and interaction_number > 0):
                #follow
                follow.fol()
                interaction_number = interaction_number-1
                set_pg_value(ref - interaction_number)
            if(job_list[1] and interaction_number > 0):
                #direct message
                url = driver.current_url
                direct_messaging.message_func()
                driver.get(url)
                interaction_number = interaction_number-1
                set_pg_value(ref - interaction_number)
            #get pictures
            if(job_list[0] and interaction_number > 0):
                pictures = get_acc_pictures.get_pics(ppa)
                for pic in pictures:
                    #return if interrupted
                    if(userdata.promo_running_flag == False):
                        return
                    driver.get(pic)
                    if(job_list[0] and interaction_number > 0):
                        #like
                        like.lk()
                        interaction_number = interaction_number-1
                        set_pg_value(ref - interaction_number)
                    if(job_list[0] and interaction_number > 0):
                        #comment
                        if(comment_counter > 0):
                            comment.com(comments)
                            comment_counter = comment_counter-1
                            interaction_number = interaction_number-1
                            set_pg_value(ref - interaction_number)
                    #timeout for pic interval
                    timeout = pic_interval
                    timeout_start = time.time()
                    while time.time() < timeout_start + timeout:
                        #return if interrupted
                        if(userdata.promo_running_flag == False):
                            return
            #timeout for acc interval
            timeout = acc_interval
            timeout_start = time.time()
            while time.time() < timeout_start + timeout:
                #return if interrupted
                if(userdata.promo_running_flag == False):
                    return
    userdata.promo_running_flag = False
    set_pg_text("finished")
    