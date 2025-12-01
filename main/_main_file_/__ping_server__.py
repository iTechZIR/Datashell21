# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
#!/usr/bin/env python3

import subprocess
import platform
import argparse
from urllib.parse import urlparse
import time

def _ping_server(url):
    parsedurl = urlparse(url)
    hostname = parsedurl.hostname

    if not hostname:
        print("-  error: invalid url format")
        return False

    print(f"-  pinging server: {hostname}")
    print(f"-  from url: {url}")

    system = platform.system().lower()
    if system == 'windows':
        pingcmd = ['ping', '-n', '4', hostname]
    else:
        pingcmd = ['ping', '-c', '4', hostname]

    print(f"-  using command: {' '.join(pingcmd)}")

    starttime = time.time()

    try:
        result = subprocess.run(
            pingcmd,
            capture_output=True,
            text=True,
            timeout=15
        )
        
        endtime = time.time()
        totaltime = endtime - starttime
        print(result.stdout)

        if result.stderr:
            print(f"-  stderr: {result.stderr}")

        if result.returncode == 0:
            print(f"-  ping successful")
        else:
            print(f"-  ping failed with code: {result.returncode}")
            
        print(f"-  total execution time: {totaltime:.2f} seconds")

        outputlower = result.stdout.lower()
        if 'packet' in outputlower and 'loss' in outputlower:
            for line in result.stdout.split('\n'):
                if 'packet' in line.lower() and 'loss' in line.lower():
                    print(f"-  {line.strip()}")

        return result.returncode == 0

    except subprocess.TimeoutExpired:
        print("-  error: ping timeout after 15 seconds")
        return False
    except Exception as error:
        print(f"-  error pinging server: {error}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="server ping - ping server and check connectivity"
    )

    parser.add_argument("-url", "--url", required=True,
                       help="server url to ping")

    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════╗
║                    DATASHELL 21                      ║
║                  __ping_server__                     ║
╚══════════════════════════════════════════════════════╝
""")

    
    _ping_server(args.url)

if __name__ == "__main__":
    main()