#Python Alert Monitoring Script :
#!/usr/bin/env python3
import json
import time
import RPi.GPIO as GPIO
from gpiozero import LED
# ---------------- GPIO SETUP ----------------
GPIO.setmode(GPIO.BCM)
# LEDs
GREEN = LED(22)      # Normal state indicator
RED = LED(17)        # Attack indicator
# Passive buzzer (using PWM for loud sound)
BUZZ_PIN = 5
GPIO.setup(BUZZ_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZ_PIN, 1000)   # Base frequency
pwm.start(0)
# Suricata alert log file
EVE_LOG = "/var/log/suricata/eve.json"
# ---------------- BUZZER FUNCTION ----------------
def loud_beep(freq=1500, duration=0.25):
    pwm.ChangeFrequency(freq)
    pwm.ChangeDutyCycle(50)
    time.sleep(duration)
    pwm.ChangeDutyCycle(0)
    time.sleep(0.1)
# ---------------- NORMAL STATE ----------------
def normal_state():
    RED.off()
    pwm.ChangeDutyCycle(0)
    GREEN.on()
# ---------------- ALERT STATE ----------------
def alert_state():
    GREEN.off()
    for _ in range(5):
        RED.on()
        loud_beep(1500, 0.20)
        RED.off()
        time.sleep(0.2)
    GREEN.on()
# ---------------- MONITOR SURICATA ----------------
def monitor():
    print("Monitoring Suricata alerts... (LED + buzzer active)")
    GREEN.on()   # Normal state on boot
    with open(EVE_LOG, "r") as f:
        f.seek(0, 2)  # Move to end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.05)
                continue
            try:
                event = json.loads(line)
            except:
                continue
            if event.get("event_type") == "alert":
                sig = event["alert"]["signature"]
                print(f"ALERT: {sig}")
                alert_state()
# ---------------- MAIN ----------------
try:
    monitor()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pwm.stop()
    GPIO.cleanup()
