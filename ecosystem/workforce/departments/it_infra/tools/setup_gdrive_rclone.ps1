$ErrorActionPreference = "Stop"

$RcloneExe = "system\ops\tools\rclone\rclone.exe"

if (-not (Test-Path $RcloneExe)) {
    Write-Host "❌ Rclone chưa được cài đặt. System đang tự động tải..." -ForegroundColor Red
    New-Item -ItemType Directory -Force -Path "system\ops\tools\rclone" | Out-Null
    Invoke-WebRequest -Uri "https://downloads.rclone.org/v1.66.0/rclone-v1.66.0-windows-amd64.zip" -OutFile "system\ops\tools\rclone\rclone.zip"
    Expand-Archive -Path "system\ops\tools\rclone\rclone.zip" -DestinationPath "system\ops\tools\rclone" -Force
    Move-Item "system\ops\tools\rclone\rclone-v1.66.0-windows-amd64\rclone.exe" "system\ops\tools\rclone\rclone.exe" -Force
    Remove-Item "system\ops\tools\rclone\rclone.zip" -Force
    Remove-Item "system\ops\tools\rclone\rclone-v1.66.0-windows-amd64" -Recurse -Force
    Write-Host "✅ Install Rclone thành công!" -ForegroundColor Green
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " 🌐 OMNICLAW: THIẾT LẬP KẾT NỐI TỰ ĐỘNG TỚI GOOGLE DRIVE" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Hướng dẫn cực nhanh:"
Write-Host " 1. Khi Menu hiện ra, bạn gõ 'n' (New remote) rồi Enter."
Write-Host " 2. Đặt tên (name) bắt buộc là: gdrive"
Write-Host " 3. Mục Storage, tìm số thứ tự của Google Drive (thường là 18) và gõ vào."
Write-Host " 4. Bỏ trống (Enter) mọi ô hỏi Client ID / Client Secret."
Write-Host " 5. Type of access: Chọn số 1 (Full Access)."
Write-Host " 6. Cứ Enter bỏ qua các câu hỏi nâng cao."
Write-Host " 7. Use auto config? Chọn 'y'. Trình duyệt sẽ mở ra để bạn đăng nhập Google."
Write-Host " 8. Đồng ý cấp quyền, quay lại Console gõ 'q' lưu cấu hình là xong!"
Write-Host ""

Start-Sleep -Seconds 3
& $RcloneExe config