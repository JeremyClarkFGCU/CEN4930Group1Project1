# Project 1 - Group 1
# StreamCamera.py
# Use Raspberry Pi Zero W Camera Module to stream video to another Machine

import subprocess
import time

# RTSP Streaming Parameters
streamPort = 8554 # Safe RTSP Port

def start_rtsp_stream(): # Starts RTSP Stream using libcamera
    try:
        cmd = [ # Set stream parameters to
            'libcamera-vid',
            '-t', '0', '-v',  # 0ms timeout, Verbose output for debugging
            '--inline',
            '--listen',
            '--o', f'rtsp://0.0.0.0:{streamPort}  # Enable access from any IP'
        ]

        # Start subprocess
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print(f"RSTP stream started on rtsp://XXX.XXX.XXX.XXX:{streamPort}/stream")
        print("Use a player like VLC to view the stream")

        # Loop until interrupted

        while True:
            # stdoutput = process.stdout.readline() # read standard output
            output = process.stderr.readline() # Read from stderr

            # if stdoutput: # This was too voluminous and I commented out to avoid the additional output
                #print(stdoutput)
            if output:
                print(output.decode())  # If error, output.
            time.sleep(1)

    except KeyboardInterrupt:# Quit on Keyboard Interrupt
        print("Stopping stream.")
        process.terminate()
        process.wait()


if __name__ == '__main__':
    start_rtsp_stream()