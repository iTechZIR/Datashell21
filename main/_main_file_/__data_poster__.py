# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
#!/usr/bin/env python3

import json
import sys
import argparse
import __requests_server__ as requestsmodule
import __info_server__ as infomodule
import __ping_server__ as pingmodule

datafile = "main_data_file__data__.json"

def _load_data():
    try:
        with open(datafile, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"-  error: data file '{datafile}' not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"-  error: invalid json format in '{datafile}'")
        sys.exit(1)

def _parse_headers(headerargs):
    headers = {}
    if headerargs:
        for header in headerargs:
            if ':' in header:
                key, value = header.split(':', 1)
                headers[key.strip()] = value.strip()
    return headers

def _post_data(url, headers=None):
    datasend = _load_data()
    print(f"-  sending data to: {url}")
    return requestsmodule.sendpostrequest(url, datasend, headers)

def main():
    parser = argparse.ArgumentParser(
                description="data poster - send data from json file to server"                
    )

    parser.add_argument("-url", "--url", required=True,
                        help="server url")

    actiongroup = parser.add_mutually_exclusive_group(required=True)
    actiongroup.add_argument("-data", "--data", action="store_true",
                           help="post data from json file to server")
    actiongroup.add_argument("-info", "--info", action="store_true",
                           help="get server information")
    actiongroup.add_argument("-ping", "--ping", action="store_true",
                           help="ping server")
    actiongroup.add_argument("-request", "--request",
                           choices=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
                           help="send custom http request")

    parser.add_argument("-H", "--header", action="append",
                       help="custom headers (format: 'header-name: value')")
    parser.add_argument("-method", "--method",
                       choices=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
                       help="http method for -request option")

    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════╗
║                    DATASHELL 21                      ║
║                  __data_poster__                     ║
╚══════════════════════════════════════════════════════╝
""")


    parsedheaders = _parse_headers(args.header)

    if args.data:
        print("-  mode: data post")
        response = _post_data(args.url, parsedheaders)
    
    elif args.info:
        print("-  mode: server info")
        infomodule._get_server(args.url)
    
    elif args.ping:
        print("-  mode: ping server")
        pingmodule._ping_server(args.url)
    
    elif args.request:
        print(f"-  mode: custom request ({args.request})")
        methodtouse = args.request
        if args.method:
            methodtouse = args.method
            print(f"-  using method: {methodtouse}")
        
        datatosend = None
        if methodtouse in ["POST", "PUT"]:
            try:
                datatosend = _load_data()
                print(f"-  loaded data from json file for {methodtouse} request")
            except:
                print(f"-  warning: could not load data for {methodtouse} request")
        
        requestsmodule._send_custom_request(args.url, methodtouse, datatosend, parsedheaders)

if __name__ == "__main__":
    main()
