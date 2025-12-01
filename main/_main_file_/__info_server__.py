# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
#!/usr/bin/env python3

import requests
import argparse
from urllib.parse import urlparse

def _get_server(url):
    print(f"-  getting server info from: {url}")

    try:
        response = requests.head(url, timeout=5, allow_redirects=True)

        print(f"-  server information:")
        print(f"-  url: {url}")
        print(f"-  final url: {response.url}")
        print(f"-  status: {response.status_code}")

        parsedurl = urlparse(url)
        print(f"-  scheme: {parsedurl.scheme}")
        print(f"-  hostname: {parsedurl.hostname}")
        if parsedurl.port:
            print(f"-  port: {parsedurl.port}")

        print(f"-  response headers:")
        for key, value in response.headers.items():
            print(f"-  {key}: {value}")

        commonheaders = ['server', 'data', 'content-type', 'content-length']
        print(f"\n-  important headers:")
        for header in commonheaders:
            if header in response.headers:
                print(f"-  {header}: {response.headers[header]}")

        return True

    except requests.exceptions.RequestException as error:
        print(f"-  error getting server info: {error}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="server info - get server headers and information"
    )

    parser.add_argument("-url", "--url", required=True,
                       help="server url to check")

    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════╗
║                    DATASHELL 21                      ║
║                  __info_server__                     ║
╚══════════════════════════════════════════════════════╝
""")


    _get_server(args.url)

if __name__ == "__main__":
    main()