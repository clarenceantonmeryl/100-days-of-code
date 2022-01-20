from linkedin_bot import LinkedInBot

linkedin_bot = LinkedInBot()
linkedin_bot.login()
linkedin_bot.save_job()










































'''
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in") # find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(3)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(3)

save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_button.click()

time.sleep(5)
'''