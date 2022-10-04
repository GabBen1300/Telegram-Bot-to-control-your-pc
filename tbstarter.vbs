Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run """" & "C:\Program Files\Tbot\tb.exe" & """", 0
Set WShell = Nothing