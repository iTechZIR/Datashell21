# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
#!/usr/bin/env python3

import requests
import json
import argparse

def _send_post_request(url, data, headers=None):
    try:
        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=10
        )

        _print_response(response)
        return response

    except requests.exceptions.RequestException as error:
        print(f"-  error sending request: {error}")
        return None

def _send_custom_request(url, method, data=None, headers=None):
    method = method.upper()
    print(f"-  sending {method} request to: {url}")

    if data:
        print(f"-  request data: {json.dumps(data, indent=2)}")

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, timeout=10)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, timeout=10)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=10)
        elif method == "HEAD":
            response = requests.head(url, headers=headers, timeout=10)
        elif method == "OPTIONS":
            response = requests.options(url, headers=headers, timeout=10)
        else:
            print(f"-  error: unsupported method '{method}'")
            return None

        _print_response(response)
        return response

    except requests.exceptions.RequestException as error:
        print(f"-  error sending request: {error}")
        return None

def _print_response(response):
    print(f"\n-  response status: {response.status_code}")
    print(f"-  response headers:")
    for key, value in response.headers.items():
        print(f"-  {key}: {value}")

    try:
        responsejson = response.json()
        print(f"-  response body (json):")
        print(json.dumps(responsejson, indent=2))
    except:
        text = response.text
        preview = text[:500]
        print(f"-  response body (text, first 500 chars):")
        print(preview)
        if len(text) > 500:
            print(f"... (total {len(text)} characters)")

def main():
    parser = argparse.ArgumentParser(
        description="requests module - send http requests"
    )
    
    parser.add_argument("-url", "--url", required=True,
                       help="server url")
    parser.add_argument("-method", "--method", default="GET",
                       choices=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
                       help="http method to use")
    parser.add_argument("-H", "--header", action="append",
                       help="custom headers (format: 'header-name: value')")
    
    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════╗
║                    DATASHELL 21                      ║
║                 __requests_server__                  ║
╚══════════════════════════════════════════════════════╝
""")


    headers = {}
    if args.header:
        for header in args.header:
            if ':' in header:
                key, value = header.split(':', 1)
                headers[key.strip()] = value.strip()
    
    _send_custom_request(args.url, args.method, None, headers)


if __name__ == "__main__":
    main()