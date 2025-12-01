#!/usr/bin/env python3
# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c

import sys
import os
import subprocess

def main():
    
    print("""
╔══════════════════════════════════════════════════════╗
║                    DATASHELL 21                      ║
║                    _Starter.py                       ║
╚══════════════════════════════════════════════════════╝
""")
    
    args = sys.argv[1:]
    
    if not args:
        print("-  usage: python _Starter.py [options]")
        print("-  example: python _Starter.py -url http://example.com -ping")
        print("-  example: python _Starter.py -url http://example.com/api -data")
        return
    
    mainscriptpath = "main\\_main_file_\\__data_poster__.py"
    
    if not os.path.exists(mainscriptpath):
        print(f"-  error: file not found: {mainscriptpath}")
        return
    
    try:
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        cmd = [sys.executable, mainscriptpath] + args
        
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=30,
            encoding='utf-8',
            errors='replace', 
            env=env
        )
        
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("-  stderr:", result.stderr)
        
    except subprocess.TimeoutExpired:
        print("-  error: command timeout after 30 seconds")
    except Exception as e:
        print(f"-  error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
