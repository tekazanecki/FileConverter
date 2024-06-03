# PowerShell script to capture the path of a selected file and place it on the clipboard
Add-Type -AssemblyName System.Windows.Forms

$files = @()
$DropList = New-Object System.Windows.Forms.DataObject
$DropList = [System.Windows.Forms.Clipboard]::GetDataObject()
$DropList.GetDataPresent([Windows.Forms.DataFormats]::FileDrop)

if ($DropList.GetDataPresent([Windows.Forms.DataFormats]::FileDrop)) {
    $files = $DropList.GetData([Windows.Forms.DataFormats]::FileDrop)
}

if ($files.Length -eq 1) {
    $file = $files[0]
    Set-Clipboard -Value $file
    Write-Output "Selected file path: $file"
} else {
    Write-Output "No file or multiple files selected."
}