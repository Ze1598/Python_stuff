import os
#Change the directory to where the wanted file is located
os.chdir("C:\\Users\\ze179\\Desktop\\")
#Print the current directory
print('Current directory: ', os.getcwd())
import Ze1598Bot_credentials as bot_info
print('Consumer key:', bot_info.consumer_key)
print('Consumer secret:', bot_info.consumer_secret)
print('Access token:', bot_info.access_token)
print('Access_token_secret:', bot_info.access_token_secret)