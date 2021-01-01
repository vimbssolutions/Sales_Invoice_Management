@ECHO OFF
start cmd.exe /C "python manage.py runserver 7004 && cd D:\D1\ && D:"
timeout 10
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:7004/"