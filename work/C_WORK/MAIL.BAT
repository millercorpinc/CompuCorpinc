@echo off
if "%1"=="" goto help
if /I "%1"=="LIST" goto list
if /I "%1"=="READ" goto read
if /I "%1"=="REPLY" goto reply
if /I "%1"=="ARCHIVE" goto archive
if /I "%1"=="HELP" goto help
goto help

:list
echo.
echo INBOX:
dir /b MAIL\INBOX\*.MSG
echo.
goto end

:read
if "%2"=="" goto help
echo.
type MAIL\INBOX\%2
echo.
goto end

:reply
if "%2"=="" goto help
echo Creating reply template in OUTBOX...
echo ID: REPLY_TO_%2> MAIL\OUTBOX\RE_%2
echo TO: (fill me in)>> MAIL\OUTBOX\RE_%2
echo FROM: aiworker@company.com>> MAIL\OUTBOX\RE_%2
echo DATE: (fill me in)>> MAIL\OUTBOX\RE_%2
echo SUBJECT: RE: (fill me in)>> MAIL\OUTBOX\RE_%2
echo.>> MAIL\OUTBOX\RE_%2
echo BODY:>> MAIL\OUTBOX\RE_%2
echo.>> MAIL\OUTBOX\RE_%2
echo END:>> MAIL\OUTBOX\RE_%2
echo Done: MAIL\OUTBOX\RE_%2
goto end

:archive
if "%2"=="" goto help
echo Archiving %2 ...
move MAIL\INBOX\%2 MAIL\ARCHIVE\%2 >nul
echo Done.
goto end

:help
echo.
echo MAIL commands:
echo   MAIL LIST
echo   MAIL READ  filename.MSG
echo   MAIL REPLY filename.MSG
echo   MAIL ARCHIVE filename.MSG
echo.
echo Example:
echo   MAIL LIST
echo   MAIL READ  20260222_091400_task-inventory__2026-02-22-001.MSG
echo.
:end
