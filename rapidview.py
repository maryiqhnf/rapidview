import ntplib
from time import ctime
import os
import ctypes

def sync_time_with_ntp(server='pool.ntp.org'):
    try:
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        print(f"Time from {server}: {ctime(response.tx_time)}")
        
        # Check if we are on Windows
        if os.name == 'nt':
            # Convert NTP time to system time format (seconds since 1/1/1601)
            ntp_time = response.tx_time + 11644473600
            # Convert to 100-nanosecond intervals
            ntp_time *= 10000000
            # Set system time
            ctypes.windll.kernel32.SetSystemTimeAsFileTime(ctypes.byref(ctypes.c_ulonglong(int(ntp_time))))
            print("System time synchronized successfully.")
        else:
            print("This function only works on Windows systems.")
    except Exception as e:
        print(f"Failed to sync time: {e}")

if __name__ == "__main__":
    sync_time_with_ntp()