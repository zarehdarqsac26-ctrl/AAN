[app]

title = YouTube to MP3
package.name = youtubetomp3
package.domain = org.al.youtubetomp3
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf
version = 1.0
requirements = python3,kivy,yt-dlp,ffmpeg
orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Keep Android build compatible with modern devices while avoiding unnecessary permissions.
android.api = 35
android.minapi = 23

[buildozer]
log_level = 2
warn_on_root = 1
