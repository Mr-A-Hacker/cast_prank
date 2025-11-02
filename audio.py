import pychromecast
import time

# Discover devices
chromecasts, browser = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if "Dining Room speaker" in cc.name)
cast.wait()

# Cast TTS audio
mc = cast.media_controller
mc.play_media('http://192.168.2.181:8080/hacked_by_mr_a.mp3', 'audio/mp3')
mc.block_until_active()
mc.play()

print("🔊 Casting TTS alert... Press Ctrl + C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Stopping playback...")
    mc.stop()
