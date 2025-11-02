import pychromecast
import time

# Discover devices
chromecasts, browser = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if "Dining Room speaker" in cc.name)
cast.wait()

# Cast audio
mc = cast.media_controller
mc.play_media('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3', 'audio/mp3')
mc.block_until_active()
mc.play()

print("🎶 Casting audio... Press Ctrl + C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Stopping playback...")
    mc.stop()
