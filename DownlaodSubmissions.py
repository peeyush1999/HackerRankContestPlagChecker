import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#import pyautogui
import random
import xlrd
import sys

#./moss -l cc -c "samAndGift" *.cpp


#wget -r -np <moss url>



probUrl=sys.argv[1]
probUrl=probUrl+sys.argv[2]
probName=sys.argv[2]

acc="/hackers/"
suff="/download_solution"
user="2021201053_aqib"
nurl=probUrl+acc+user+suff
print(nurl)


data = xlrd.open_workbook('password.xls')
table = data.sheet_by_name(u'Sheet1')

userId="" #input-4
password=""#input-5


def processdata():
    table = data.sheet_by_name(u'Sheet2')
    #driver = webdriver.Chrome(executable_path=r'webdrivers/chromedriver.exe')
        #/home/peeyushsahu/Desktop/DownloadSubmission

    driver = webdriver.Firefox(executable_path=r'/home/peeyushsahu/Desktop/DownloadSubmission/geckodriver');
    driver.maximize_window()

    '''
    time.sleep(0.5)
    driver.get('https://www.hackerrank.com/auth/login/2021-dsa-lab-3')
    
    time.sleep(2)
    driver.find_element_by_name('username').send_keys(userId)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(1)
    driver.execute_script("document.getElementsByClassName('ui-btn ui-btn-large ui-btn-primary auth-button ui-btn-styled')[0].click()");    
    time.sleep(1)

    input("Wait")
        '''
    #https://www.hackerrank.com/rest/contests/2021-dsa-lab-3/challenges/sam-and-the-gift/hackers/2021201053_aqib/download_solution
    #probUrl="https://www.hackerrank.com/rest/contests/2021-dsa-lab-3/challenges/assembly-2/"
    #acc="hackers/"
    #user="2021201053_aqib"
    #suff="/download_solution"
    
    global user
    nurl=probUrl+acc+user+suff
    print(nurl)
    


    driver.get(nurl)



    
    
    for row in range(table.nrows):
        name = str(table.cell(row,0).value)
        name = name.strip()
        
        print(user)
        user=name
        nurl=probUrl+acc+user+suff

        driver.get(nurl)
        
        #print(driver.find_element_by_xpath("/html/body/pre").text)
        txt=driver.find_element_by_xpath("/html/body/pre").text
        
        if (txt == ""):
        	continue;

        
        with open(probName+'/'+name+'_sol.cpp', 'w') as f:
            f.write(txt)
                
        

    driver.quit()        
        
        

processdata()

#=====================================================


print("Completed!!!!")


  
