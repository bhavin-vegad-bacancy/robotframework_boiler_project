*** Variables ***
${base_url}     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#${USERNAME_XPATH}    //input[@placeholder='Username']
${USERNAME_XPATH}    //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input
#${PASSWORD_XPATH}    //input[@placeholder='Password']
${PASSWORD_XPATH}    //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input
${LOGIN_BTN_XPATH}   //button[@type='submit']
${DASHBOARD_PAGE_XPATH}    //h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
${invalidelement_XPATH}     //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]