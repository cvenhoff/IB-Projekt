import login_ui
import dashboard_ui
import profiledata
import promo
import time
import wbdriver
import userdata
import unfollow
import threading
import load_set_data

# message
print("starting browser remote... pease don't close this window.")
# load data
load_set_data.get_data()
# login
login = login_ui.login_ui_class()
login.login_()
# dashboard
dashboard = dashboard_ui.dashboard_ui_class()
dashboard.dashboard_()
