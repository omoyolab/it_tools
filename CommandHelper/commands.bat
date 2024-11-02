@echo off
::  Author: AxelrMSFT
::  V.2.23
::  Tested in: Win11, 10 & Server SKUs

:home
cls
Mode con cols=100 lines=50 & color 0B
echo Please select the task you wish to run.
echo Pick one: 
 echo.
 echo  1. Delete Non-trusted web History(low level hidden clean up) 
 echo  2. Delete History 
 echo  3. Delete Cookies 
 echo  4. Delete Temporary Internet Files 
 echo  5. Delete Form Data 
 echo  6. Delete Stored Passwords 
 echo  7. Delete All 
 echo  8. Delete All "Also delete files and settings stored by add-ons"
 echo  9. Delete IE10 and 9 Temporary Internet Files
 echo  10. Delete Browsing History Dialog
 echo  11. Show Website Data Settings
 echo  12. Launch Security Dialog
 echo  13. Launch Popup Window Management Dialog
 echo  14. Launch Privacy Dialog
 echo  15. Launch Site Cert Dialog
 echo  16. Launch Per Site Privacy Action Dialog
 echo  17. Launch Connection Dialog
 echo  18. Open Fonts Dialog
 echo  19. Launch Internet Control Panel
 echo  20. To clear IE Downloaded Files
 echo  21. To Preserve Favorites website data 
 echo  22. To clear IE browsing history 
 echo  23. Programs Tab
 echo  24. Reset IE to Defaults
 echo  25. Terminate all running MSEdge.exe  
 echo  26. Terminate all IExplore.exe  
 echo  27. Terminate all running Chrome.exe  
 echo  28. Terminate all running firefox.exe 
 echo  29. Terminate all running opera.exe
 echo  30. Terminal ALL browsers found (IExplore.exe, Chrome.exe, MSEdge.exe, Firefox.exe, opera.exe)
 echo  31. Terminate ms-teams.exe
 echo  77. EXIT
:choice
 set /P CH=[1-23]

if "%CH%"=="1" set x=del /s /q C:\Users\%username%\AppData\Local\Microsoft\Windows\History\low\* /ah 
 if "%CH%"=="2" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 1 
 if "%CH%"=="3" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 2 
 if "%CH%"=="4" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8 
 if "%CH%"=="5" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 16 
 if "%CH%"=="6" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 32 
 if "%CH%"=="7" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255 
 if "%CH%"=="8" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 4351 
 if "%CH%"=="9" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 9  
 if "%CH%"=="10" set x=RunDll32.exe InetCpl.cpl,ShowDeleteBrowsingHistoryDialog
 if "%CH%"=="11" set x=RunDll32.exe InetCpl.cpl,ShowWebsiteDataSettings
 if "%CH%"=="12" set x=RunDll32.exe InetCpl.cpl,LaunchSecurityDialog
 if "%CH%"=="13" set x=RunDll32.exe InetCpl.cpl,LaunchPopupWindowManagementDialog
 if "%CH%"=="14" set x=RunDll32.exe InetCpl.cpl,LaunchPrivacyDialog
 if "%CH%"=="15" set x=RunDll32.exe InetCpl.cpl,LaunchSiteCertDialog
 if "%CH%"=="16" set x=RunDll32.exe InetCpl.cpl,LaunchPerSitePrivacyActionDialog
 if "%CH%"=="17" set x=RunDll32.exe InetCpl.cpl,LaunchConnectionDialog
 if "%CH%"=="18" set x=RunDll32.exe InetCpl.cpl,OpenFontsDialog
 if "%CH%"=="19" set x=RunDll32.exe InetCpl.cpl,LaunchInternetControlPanel
 if "%CH%"=="20" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 16384
 if "%CH%"=="21" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8192
 if "%CH%"=="22" set x=RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 193
 if "%CH%"=="23" set x=Rundll32.exe shell32.dll,Control_RunDLL inetcpl.cpl,,5
 if "%CH%"=="24" set x=rundll32.exe inetcpl.cpl ResetIEtoDefaults
 if "%CH%"=="25" set x=Taskkill /IM "msedge.exe" /f
 if "%CH%"=="26" set x=Taskkill /IM "IExplore.exe" /f
 if "%CH%"=="27" set x=Taskkill /IM "chrome.exe" /f
 if "%CH%"=="28" set x=Taskkill /IM "firefox.exe" /f
 if "%CH%"=="29" set x=Taskkill /IM "opera.exe" /f
 if "%CH%"=="30" set x=Taskkill /IM "firefox.exe" /f /t & taskkill /im "chrome.exe" /f /t & taskkill /im "IExplore.exe" /f /t & taskkill /im "msedge.exe" /f /t & taskkill /im "opera.exe" /f /t
 if "%CH%"=="31" set x=Taskkill /IM "ms-teams.exe" /f

if "%CH%"=="77" goto quit

%x%

goto Home

::Temporary Internet Files > Delete files - To delete copies of web pages, images, and media 
 ::that  are saved for faster viewing.
::Cookies > Delete cookies - To delete cookies, which are files stored on your computer by 
 ::websites to save preferences such as login information.
::History > Delete history - To delete the history of the websites you have visited.
::Form data > Delete forms - To delete all the saved information that you have typed into 
 ::forms.
::Passwords > Delete passwords - To delete all the passwords that are automatically filled in 
 ::when you log on to a website you've previously visited.
::Delete all - To delete all of the above in one operation.

::enter below in search/run to see Low  history dir if exists
::%userprofile%\AppData\Local\Microsoft\Windows\History\low

::Delete all low(untrusted history) very hidden 
 ::this will clean any unlocked  files under the dir and not delete the dir structure 
 ::del /s /q low\* /ah ::del /s /q %userprofile%\AppData\Local\Microsoft\Windows\History\low\* /ah

:: VBS to reset IE Automatically. Copy and paste in notepad and save as IEReset.vbs
:: Script start below
::'--------------------------------------------
:: 'IE Reset Automation
:: Set objAP = CreateObject("wscript.shell")
:: objAP.Run "rundll32.exe inetcpl.cpl ResetIEtoDefaults"
:: wscript.sleep 1000

:: objAP.AppActivate "Reset Internet Explorer Settings"
:: objAP.SendKeys "%r", True

:: wscript.sleep 2000

:: If objAP.AppActivate("Reset Internet Explorer Settings") Then objAP.SendKeys "%c"
:: wscript.sleep 2000

:: If objAP.AppActivate("Reset Internet Explorer Settings") Then objAP.SendKeys "%c"
:: wscript.sleep 2000

:: If objAP.AppActivate("Reset Internet Explorer Settings") Then objAP.SendKeys "%c"

goto Home