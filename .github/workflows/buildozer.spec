[app]

title = YouTube to MP3
package.name = youtubetomp3
package.domain = org.alik.youtubetomp3
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf
version = 1.0
requirements = python3,kivy,openssl,requests,yt-dlp
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a
android.api = 33
android.minapi = 23
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
