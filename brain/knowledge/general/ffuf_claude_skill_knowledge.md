---
id: ffuf-claude-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:24.122794
---

# KNOWLEDGE EXTRACT: ffuf_claude_skill
> **Extracted on:** 2026-03-30 13:16:33
> **Source:** ffuf_claude_skill

---

## File: `README.md`
```markdown
# FFUF Skill for Claude Code

A Claude Code skill that integrates the powerful web fuzzer [ffuf](https://github.com/ffuf/ffuf) (Fuzz Faster U Fool) for web security testing and reconnaissance tasks.

## Overview

This skill enables Claude Code to perform intelligent web fuzzing operations using ffuf, making it easier to discover hidden directories, files, subdomains, and API endpoints.

## Prerequisites

- [ffuf](https://github.com/ffuf/ffuf) must be installed on your system
- Claude Desktop application
- Appropriate authorization to test target systems

### Installing ffuf

**macOS:**
```bash
brew install ffuf
```

**Linux:**
```bash
go install github.com/ffuf/ffuf/v2@latest
```

**Other methods:** See the [official ffuf repository](https://github.com/ffuf/ffuf)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jthack/ffuf_claude_skill
```

2. Copy the skill folder to Claude Code's skills directory:
```bash
mkdir -p ~/.claude/skills
cp -r ffuf_claude_skill/ffuf-skill ~/.claude/skills/
```

3. The skill is now available for Claude Code to use!

## Usage

Once installed, you can ask Claude Code to perform ffuf operations naturally:

- "Fuzz the /api endpoint on example.com for hidden paths"
- "Enumerate subdomains for target.com"
- "Find common directories on https://example.com"
- "Test for backup files on the /admin path"

Claude will automatically invoke the ffuf skill and interpret the results for you.

## Features

- **Intelligent Fuzzing**: Claude interprets your testing goals and configures ffuf appropriately
- **Result Analysis**: Automatic filtering and analysis of ffuf output
- **Safe Defaults**: Includes rate limiting and sensible defaults to avoid aggressive testing
- **Wordlist Management**: Helps select appropriate wordlists for different testing scenarios

## Safety & Ethics

**IMPORTANT**: This skill is designed for defensive security purposes only:

- Only test systems you own or have explicit permission to test
- Respect rate limits and avoid causing service disruption
- Follow responsible disclosure practices
- Comply with applicable laws and regulations

Unauthorized testing of systems is illegal and unethical.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for complying with all applicable laws and obtaining proper authorization before testing any systems.
```

## File: `ffuf-skill/ffuf_helper.py`
```python
#!/usr/bin/env python3
"""
FFUF Helper Script - Assists with common ffuf tasks
"""

import json
import sys
import argparse
from pathlib import Path
from collections import Counter


def analyze_results(json_file):
    """Analyze ffuf JSON results and find interesting anomalies"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    results = data.get('results', [])
    
    if not results:
        print("No results found in JSON file")
        return
    
    print(f"\n=== FFUF Results Analysis ===")
    print(f"Total results: {len(results)}")
    
    # Status code distribution
    status_codes = Counter(r['status'] for r in results)
    print(f"\n[+] Status Code Distribution:")
    for code, count in sorted(status_codes.items()):
        print(f"    {code}: {count}")
    
    # Response size analysis
    sizes = [r['length'] for r in results]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    print(f"\n[+] Response Sizes:")
    print(f"    Average: {avg_size:.0f} bytes")
    print(f"    Min: {min(sizes)} bytes")
    print(f"    Max: {max(sizes)} bytes")
    
    # Find anomalies
    print(f"\n[+] Interesting Findings:")
    
    # Look for different status codes
    interesting_codes = [r for r in results if r['status'] not in [404, 403]]
    if interesting_codes:
        print(f"    - Found {len(interesting_codes)} results with interesting status codes")
        for r in interesting_codes[:10]:  # Show first 10
            print(f"      {r['status']} - {r['url']} ({r['length']} bytes)")
    
    # Look for size anomalies (significantly different from average)
    size_threshold = avg_size * 0.5  # 50% difference
    anomalous_sizes = [r for r in results if abs(r['length'] - avg_size) > size_threshold]
    if anomalous_sizes:
        print(f"    - Found {len(anomalous_sizes)} results with anomalous sizes")
        for r in sorted(anomalous_sizes, key=lambda x: x['length'], reverse=True)[:10]:
            print(f"      {r['status']} - {r['url']} ({r['length']} bytes)")
    
    # Look for interesting words in URLs
    interesting_keywords = ['admin', 'api', 'backup', 'config', 'dev', 'test', 
                           'staging', 'git', 'env', 'sql', 'db', 'key', 'secret',
                           'password', 'token', 'internal', 'private']
    interesting_urls = [r for r in results 
                       if any(kw in r['url'].lower() for kw in interesting_keywords)]
    if interesting_urls:
        print(f"    - Found {len(interesting_urls)} results with interesting keywords")
        for r in interesting_urls[:10]:
            print(f"      {r['status']} - {r['url']}")
    
    # Timing anomalies (if available)
    if results and 'duration' in results[0]:
        durations = [r['duration'] for r in results]
        avg_duration = sum(durations) / len(durations)
        slow_requests = [r for r in results if r['duration'] > avg_duration * 2]
        if slow_requests:
            print(f"    - Found {len(slow_requests)} slow responses (potential SQLi, etc.)")
            for r in sorted(slow_requests, key=lambda x: x['duration'], reverse=True)[:5]:
                print(f"      {r['status']} - {r['url']} ({r['duration']}ms)")


def create_request_file(output_file, method='GET', url='/', headers=None, body=None):
    """Create a template req.txt file"""
    
    # Parse URL to get host and path
    if '://' in url:
        protocol, rest = url.split('://', 1)
        if '/' in rest:
            host, path = rest.split('/', 1)
            path = '/' + path
        else:
            host = rest
            path = '/'
    else:
        host = 'target.com'
        path = url if url.startswith('/') else '/' + url
    
    # Start building the request
    lines = [f"{method} {path} HTTP/1.1"]
    lines.append(f"Host: {host}")
    lines.append("User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
    
    # Add headers
    if headers:
        for header in headers:
            lines.append(header)
    
    # Add blank line before body
    lines.append("")
    
    # Add body if present
    if body:
        lines.append(body)
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"[+] Created request template: {output_file}")
    print(f"[!] Don't forget to add the FUZZ keyword where you want to fuzz!")


def generate_wordlist(output_file, type='numbers', start=1, end=1000):
    """Generate common wordlists"""
    with open(output_file, 'w') as f:
        if type == 'numbers':
            for i in range(start, end + 1):
                f.write(f"{i}\n")
        elif type == 'padded':
            width = len(str(end))
            for i in range(start, end + 1):
                f.write(f"{str(i).zfill(width)}\n")
    
    print(f"[+] Generated {type} wordlist: {output_file}")
    print(f"    Range: {start}-{end}")


def main():
    parser = argparse.ArgumentParser(
        description='FFUF Helper - Analyze results and create templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze ffuf JSON results
  %(prog)s analyze results.json
  
  # Create a request template
  %(prog)s create-req -o req.txt -m POST -u "https://api.target.com/users" \\
      -H "Authorization: Bearer TOKEN" -d '{"action":"FUZZ"}'
  
  # Generate number wordlist for IDOR testing
  %(prog)s wordlist -o ids.txt -t numbers -s 1 -e 10000
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze ffuf JSON results')
    analyze_parser.add_argument('json_file', help='Path to ffuf JSON output file')
    
    # Create request command
    req_parser = subparsers.add_parser('create-req', help='Create req.txt template')
    req_parser.add_argument('-o', '--output', required=True, help='Output file path')
    req_parser.add_argument('-m', '--method', default='GET', help='HTTP method')
    req_parser.add_argument('-u', '--url', default='/', help='URL or path')
    req_parser.add_argument('-H', '--header', action='append', dest='headers', 
                           help='Add header (can be used multiple times)')
    req_parser.add_argument('-d', '--data', help='Request body')
    
    # Generate wordlist command
    wl_parser = subparsers.add_parser('wordlist', help='Generate wordlist')
    wl_parser.add_argument('-o', '--output', required=True, help='Output file path')
    wl_parser.add_argument('-t', '--type', choices=['numbers', 'padded'], 
                          default='numbers', help='Wordlist type')
    wl_parser.add_argument('-s', '--start', type=int, default=1, help='Start number')
    wl_parser.add_argument('-e', '--end', type=int, default=1000, help='End number')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'analyze':
        analyze_results(args.json_file)
    elif args.command == 'create-req':
        create_request_file(args.output, args.method, args.url, 
                          args.headers, args.data)
    elif args.command == 'wordlist':
        generate_wordlist(args.output, args.type, args.start, args.end)


if __name__ == '__main__':
    main()
```

## File: `ffuf-skill/SKILL.md`
```markdown
---
name: ffuf-web-fuzzing
description: Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and result analysis
---

# FFUF (Fuzz Faster U Fool) Skill

## Overview
FFUF is a fast web fuzzer written in Go, designed for discovering hidden content, directories, files, subdomains, and testing for vulnerabilities during penetration testing. It's significantly faster than traditional tools like dirb or dirbuster.

## Installation
```bash
# Using Go
go install github.com/ffuf/ffuf/v2@latest

# Using Homebrew (macOS)
brew install ffuf

# Binary download
# Download from: https://github.com/ffuf/ffuf/releases/latest
```

## Core Concepts

### The FUZZ Keyword
The `FUZZ` keyword is used as a placeholder that gets replaced with entries from your wordlist. You can place it anywhere:
- URLs: `https://target.com/FUZZ`
- Headers: `-H "Host: FUZZ"`
- POST data: `-d "username=admin&password=FUZZ"`
- Multiple locations with custom keywords: `-w wordlist.txt:CUSTOM` then use `CUSTOM` instead of `FUZZ`

### Multi-wordlist Modes
- **clusterbomb**: Tests all combinations (default) - cartesian product
- **pitchfork**: Iterates through wordlists in parallel (1-to-1 matching)
- **sniper**: Tests one position at a time (for multiple FUZZ positions)

## Common Use Cases

### 1. Directory and File Discovery
```bash
# Basic directory fuzzing
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ

# With file extensions
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -e .php,.html,.txt,.pdf

# Colored and verbose output
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -c -v

# With recursion (finds nested directories)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -recursion -recursion-depth 2
```

### 2. Subdomain Enumeration
```bash
# Virtual host discovery
ffuf -w /path/to/subdomains.txt -u https://target.com -H "Host: FUZZ.target.com" -fs 4242

# Note: -fs 4242 filters out responses of size 4242 (adjust based on default response size)
```

### 3. Parameter Fuzzing
```bash
# GET parameter names
ffuf -w /path/to/params.txt -u https://target.com/script.php?FUZZ=test_value -fs 4242

# GET parameter values
ffuf -w /path/to/values.txt -u https://target.com/script.php?id=FUZZ -fc 401

# Multiple parameters
ffuf -w params.txt:PARAM -w values.txt:VAL -u https://target.com/?PARAM=VAL -mode clusterbomb
```

### 4. POST Data Fuzzing
```bash
# Basic POST fuzzing
ffuf -w /path/to/passwords.txt -X POST -d "username=admin&password=FUZZ" -u https://target.com/login.php -fc 401

# JSON POST data
ffuf -w entries.txt -u https://target.com/api -X POST -H "Content-Type: application/json" -d '{"name": "FUZZ", "key": "value"}' -fr "error"

# Fuzzing multiple POST fields
ffuf -w users.txt:USER -w passes.txt:PASS -X POST -d "username=USER&password=PASS" -u https://target.com/login -mode pitchfork
```

### 5. Header Fuzzing
```bash
# Custom headers
ffuf -w /path/to/wordlist.txt -u https://target.com -H "X-Custom-Header: FUZZ"

# Multiple headers
ffuf -w /path/to/wordlist.txt -u https://target.com -H "User-Agent: FUZZ" -H "X-Forwarded-For: 127.0.0.1"
```

## Filtering and Matching

### Matchers (Include Results)
- `-mc`: Match status codes (default: 200-299,301,302,307,401,403,405,500)
- `-ml`: Match line count
- `-mr`: Match regex
- `-ms`: Match response size
- `-mt`: Match response time (e.g., `>100` or `<100` milliseconds)
- `-mw`: Match word count

### Filters (Exclude Results)
- `-fc`: Filter status codes (e.g., `-fc 404,403,401`)
- `-fl`: Filter line count
- `-fr`: Filter regex (e.g., `-fr "error"`)
- `-fs`: Filter response size (e.g., `-fs 42,4242`)
- `-ft`: Filter response time
- `-fw`: Filter word count

### Auto-Calibration (USE BY DEFAULT!)
**CRITICAL:** Always use `-ac` unless you have a specific reason not to. This is especially important when having Claude analyze results, as it dramatically reduces noise and false positives.

```bash
# Auto-calibration - ALWAYS USE THIS
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -ac

# Per-host auto-calibration (useful for multiple hosts)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -ach

# Custom auto-calibration string (for specific patterns)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -acc "404NotFound"
```

**Why `-ac` is essential:**
- Automatically detects and filters repetitive false positive responses
- Removes noise from dynamic websites with random content
- Makes results analysis much easier for both humans and Claude
- Prevents thousands of identical 404/403 responses from cluttering output
- Adapts to the target's specific behavior

**When Claude analyzes your ffuf results, `-ac` is MANDATORY** - without it, Claude will waste time sifting through thousands of false positives instead of finding the interesting anomalies.

## Rate Limiting and Timing

### Rate Control
```bash
# Limit to 2 requests per second (stealth mode)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -rate 2

# Add delay between requests (0.1 to 2 seconds random)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -p 0.1-2.0

# Set number of concurrent threads (default: 40)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -t 10
```

### Time Limits
```bash
# Maximum total execution time (60 seconds)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -maxtime 60

# Maximum time per job (useful with recursion)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -maxtime-job 60 -recursion
```

## Output Options

### Output Formats
```bash
# JSON output
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -o results.json

# HTML output
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -of html -o results.html

# CSV output
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -of csv -o results.csv

# All formats
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -of all -o results

# Silent mode (no progress, only results)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -s

# Pipe to file with tee
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -s | tee results.txt
```

## Advanced Techniques

### Using Raw HTTP Requests (Critical for Authenticated Fuzzing)
This is one of the most powerful features of ffuf, especially for authenticated requests with complex headers, cookies, or tokens.

**Workflow:**
1. Capture a full authenticated request (from Burp Suite, browser DevTools, etc.)
2. Save it to a file (e.g., `req.txt`)
3. Replace the value you want to fuzz with the `FUZZ` keyword
4. Use the `--request` flag

```bash
# From a file containing raw HTTP request
ffuf --request req.txt -w /path/to/wordlist.txt -ac
```

**Example req.txt file:**
```http
POST /api/v1/users/FUZZ HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Cookie: session=abc123xyz; csrftoken=def456
Content-Type: application/json
Content-Length: 27

{"action":"view","id":"1"}
```

**Use Cases:**
- Fuzzing authenticated endpoints with complex auth headers
- Testing API endpoints with JWT tokens
- Fuzzing with CSRF tokens, session cookies, and custom headers
- Testing endpoints that require specific User-Agents or Accept headers
- POST/PUT/DELETE requests with authentication

**Pro Tips:**
- You can place FUZZ in multiple locations: URL path, headers, body
- Use `-request-proto https` if needed (default is https)
- Always use `-ac` to filter out authenticated "not found" or error responses
- Great for IDOR testing: fuzz user IDs, document IDs, etc. in authenticated contexts

```bash
# Common authenticated fuzzing patterns
ffuf --request req.txt -w user_ids.txt -ac -mc 200 -o results.json

# With multiple FUZZ positions using custom keywords
ffuf --request req.txt -w endpoints.txt:ENDPOINT -w ids.txt:ID -mode pitchfork -ac
```

### Proxy Usage
```bash
# HTTP proxy (useful for Burp Suite)
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -x http://127.0.0.1:8080

# SOCKS5 proxy
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -x socks5://127.0.0.1:1080

# Replay matched requests through proxy
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -replay-proxy http://127.0.0.1:8080
```

### Cookie and Authentication
```bash
# Using cookies
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -b "sessionid=abc123; token=xyz789"

# Client certificate authentication
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -cc client.crt -ck client.key
```

### Encoding
```bash
# URL encoding
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -enc 'FUZZ:urlencode'

# Multiple encodings
ffuf -w /path/to/wordlist.txt -u https://target.com/FUZZ -enc 'FUZZ:urlencode b64encode'
```

### Testing for Vulnerabilities
```bash
# SQL injection testing
ffuf -w sqli_payloads.txt -u https://target.com/page.php?id=FUZZ -fs 1234

# XSS testing
ffuf -w xss_payloads.txt -u https://target.com/search?q=FUZZ -mr "<script>"

# Command injection
ffuf -w cmdi_payloads.txt -u https://target.com/execute?cmd=FUZZ -fr "error"
```

### Batch Processing Multiple Targets
```bash
# Process multiple URLs
cat targets.txt | xargs -I@ sh -c 'ffuf -w wordlist.txt -u @/FUZZ -ac'

# Loop through multiple targets with results
for url in $(cat targets.txt); do 
    ffuf -w wordlist.txt -u $url/FUZZ -ac -o "results_$(echo $url | md5sum | cut -d' ' -f1).json"
done
```

## Best Practices

### 1. ALWAYS Use Auto-Calibration
Use `-ac` by default for every scan. This is non-negotiable for productive pentesting:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -ac
```

### 2. Use Raw Requests for Authentication
Don't struggle with command-line flags for complex auth. Capture the full request and use `--request`:
```bash
# 1. Capture authenticated request from Burp/DevTools
# 2. Save to req.txt with FUZZ keyword in place
# 3. Run with -ac
ffuf --request req.txt -w wordlist.txt -ac -o results.json
```

### 3. Use Appropriate Wordlists
- **Directory discovery**: SecLists Discovery/Web-Content (raft-large-directories.txt, directory-list-2.3-medium.txt)
- **Subdomains**: SecLists Discovery/DNS (subdomains-top1million-5000.txt)
- **Parameters**: SecLists Discovery/Web-Content (burp-parameter-names.txt)
- **Usernames**: SecLists Usernames
- **Passwords**: SecLists Passwords
- Source: https://github.com/danielmiessler/SecLists

### 3. Rate Limiting for Stealth
Use `-rate` to avoid triggering WAF/IDS or overwhelming the server:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -rate 2 -t 10
```

### 4. Filter Strategically
- Check the default response first to identify common response sizes, status codes, or patterns
- Use `-fs` to filter by size or `-fc` to filter by status code
- Combine filters: `-fc 403,404 -fs 1234`

### 5. Save Results Appropriately
Always save results to a file for later analysis:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -o results.json -of json
```

### 6. Use Interactive Mode
Press ENTER during execution to drop into interactive mode where you can:
- Adjust filters on the fly
- Save current results
- Restart the scan
- Manage the queue

### 7. Recursion Depth
Be careful with recursion depth to avoid getting stuck in infinite loops or overwhelming the server:
```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -recursion -recursion-depth 2 -maxtime-job 120
```

## Common Patterns and One-Liners

### Quick Directory Scan
```bash
ffuf -w ~/wordlists/common.txt -u https://target.com/FUZZ -mc 200,301,302,403 -ac -c -v
```

### Comprehensive Scan with Extensions
```bash
ffuf -w ~/wordlists/raft-large-directories.txt -u https://target.com/FUZZ -e .php,.html,.txt,.bak,.old -ac -c -v -o results.json
```

### Authenticated Fuzzing (Raw Request)
```bash
# 1. Save your authenticated request to req.txt with FUZZ keyword
# 2. Run:
ffuf --request req.txt -w ~/wordlists/api-endpoints.txt -ac -o results.json -of json
```

### API Endpoint Discovery
```bash
ffuf -w ~/wordlists/api-endpoints.txt -u https://api.target.com/v1/FUZZ -H "Authorization: Bearer TOKEN" -mc 200,201 -ac -c
```

### Subdomain Discovery with Auto-Calibration
```bash
ffuf -w ~/wordlists/subdomains-top5000.txt -u https://FUZZ.target.com -ac -c -v
```

### POST Login Brute Force
```bash
ffuf -w ~/wordlists/passwords.txt -X POST -d "username=admin&password=FUZZ" -u https://target.com/login -fc 401 -rate 5 -ac
```

### IDOR Testing with Auth
```bash
# Use req.txt with authenticated headers and FUZZ in the ID parameter
ffuf --request req.txt -w numbers.txt -ac -mc 200 -fw 100-200
```

## Configuration File
Create `~/.config/ffuf/ffufrc` for default settings:
```
[http]
headers = ["User-Agent: Mozilla/5.0"]
timeout = 10

[general]
colors = true
threads = 40

[matcher]
status = "200-299,301,302,307,401,403,405,500"
```

## Troubleshooting

### Too Many False Positives
- Use `-ac` for auto-calibration
- Check default response and filter by size with `-fs`
- Use regex filtering with `-fr`

### Too Slow
- Increase threads: `-t 100`
- Reduce wordlist size
- Use `-ignore-body` if you don't need response content

### Getting Blocked
- Reduce rate: `-rate 2`
- Add delays: `-p 0.5-1.5`
- Reduce threads: `-t 10`
- Randomize User-Agent
- Use proxy rotation

### Missing Results
- Check if you're filtering too aggressively
- Use `-mc all` to see all responses
- Disable auto-calibration temporarily
- Use verbose mode `-v` to see what's happening

## Resources
- Official GitHub: https://github.com/ffuf/ffuf
- Wiki: https://github.com/ffuf/ffuf/wiki
- Codingo's Guide: https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html
- Practice Lab: http://ffuf.me
- SecLists Wordlists: https://github.com/danielmiessler/SecLists

## Quick Reference Card

| Task | Command Template |
|------|------------------|
| Directory Discovery | `ffuf -w wordlist.txt -u https://target.com/FUZZ -ac` |
| Subdomain Discovery | `ffuf -w subdomains.txt -u https://FUZZ.target.com -ac` |
| Parameter Fuzzing | `ffuf -w params.txt -u https://target.com/page?FUZZ=value -ac` |
| POST Data Fuzzing | `ffuf -w wordlist.txt -X POST -d "param=FUZZ" -u https://target.com/endpoint` |
| With Extensions | Add `-e .php,.html,.txt` |
| Filter Status | Add `-fc 404,403` |
| Filter Size | Add `-fs 1234` |
| Rate Limit | Add `-rate 2` |
| Save Output | Add `-o results.json` |
| Verbose | Add `-c -v` |
| Recursion | Add `-recursion -recursion-depth 2` |
| Through Proxy | Add `-x http://127.0.0.1:8080` |

## Additional Resources

This skill includes supplementary materials in the `resources/` directory:

### Resource Files
- **WORDLISTS.md**: Comprehensive guide to SecLists wordlists, recommended lists for different scenarios, file extensions, and quick reference patterns
- **REQUEST_TEMPLATES.md**: Pre-built req.txt templates for common authentication scenarios (JWT, OAuth, session cookies, API keys, etc.) with usage examples

### Helper Script
- **ffuf_helper.py**: Python script to assist with:
  - Analyzing ffuf JSON results for anomalies and interesting findings
  - Creating req.txt template files from command-line arguments
  - Generating number-based wordlists for IDOR testing

**Helper Script Usage:**
```bash
# Analyze results to find interesting anomalies
python3 ffuf_helper.py analyze results.json

# Create authenticated request template
python3 ffuf_helper.py create-req -o req.txt -m POST -u "https://api.target.com/users" \
    -H "Authorization: Bearer TOKEN" -d '{"action":"FUZZ"}'

# Generate IDOR testing wordlist
python3 ffuf_helper.py wordlist -o ids.txt -t numbers -s 1 -e 10000
```

**When to use resources:**
- Users need wordlist recommendations → Reference WORDLISTS.md
- Users need help with authenticated requests → Reference REQUEST_TEMPLATES.md
- Users want to analyze results → Use ffuf_helper.py analyze
- Users need to generate req.txt → Use ffuf_helper.py create-req
- Users need number ranges for IDOR → Use ffuf_helper.py wordlist

## Notes for Claude
When helping users with ffuf:
1. **ALWAYS include `-ac` in every command** - This is mandatory for productive pentesting and result analysis
2. When users mention authenticated fuzzing or provide auth tokens/cookies:
   - Suggest creating a `req.txt` file with the full HTTP request
   - Show them how to insert FUZZ where they want to fuzz
   - Use `ffuf --request req.txt -w wordlist.txt -ac`
3. Always recommend starting with `-ac` for auto-calibration
4. Suggest appropriate wordlists from SecLists based on the task
5. Remind users to use rate limiting (`-rate`) for production targets
6. Encourage saving output to files for documentation: `-o results.json`
7. Suggest filtering strategies based on initial reconnaissance
8. Always use the FUZZ keyword (case-sensitive)
9. Consider stealth: lower threads, rate limiting, and delays for sensitive targets
10. For pentesting reports, use `-of html` or `-of csv` for client-friendly formats
11. **When analyzing ffuf results for users:**
    - Assume they used `-ac` (if not, results will be too noisy)
    - Focus on anomalies: different status codes, response sizes, timing
    - Look for interesting endpoints: admin, api, backup, config, .git, etc.
    - Flag potential vulnerabilities: error messages, stack traces, version info
    - Suggest follow-up fuzzing on interesting findings
```

## File: `ffuf-skill/resources/REQUEST_TEMPLATES.md`
```markdown
# Authenticated Request Templates

These are example `req.txt` templates for common authenticated fuzzing scenarios.

## Template 1: JWT Bearer Token API Request

```http
GET /api/v1/users/FUZZ HTTP/1.1
Host: api.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
Accept: application/json
Content-Type: application/json
```

**Usage:**
```bash
ffuf --request req.txt -w wordlist.txt -ac -mc 200,201 -o results.json
```

---

## Template 2: Session Cookie + CSRF Token

```http
POST /api/account/update HTTP/1.1
Host: app.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
Cookie: sessionid=abc123xyz789; csrftoken=def456uvw; preferences=theme:dark
X-CSRF-Token: def456uvw
Content-Type: application/x-www-form-urlencoded
Content-Length: 25

field=FUZZ&action=update
```

**Usage:**
```bash
ffuf --request req.txt -w payloads.txt -ac -fc 403 -o results.json
```

---

## Template 3: API Key Header

```http
GET /v2/data/FUZZ HTTP/1.1
Host: api.target.com
User-Agent: Custom-Client/1.0
X-API-Key: YOUR_API_KEY_HERE_abc123def456ghi789jkl
Accept: application/json
```

**Usage:**
```bash
ffuf --request req.txt -w endpoints.txt -ac -mc 200 -o results.json
```

---

## Template 4: Basic Auth

```http
GET /admin/FUZZ HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Accept: text/html,application/xhtml+xml
```

**Usage:**
```bash
ffuf --request req.txt -w admin-paths.txt -ac -mc 200,301,302 -o results.json
```

---

## Template 5: OAuth 2.0 Bearer

```http
GET /api/v1/resources/FUZZ HTTP/1.1
Host: api.target.com
User-Agent: OAuth-Client/2.0
Authorization: Bearer ya29.a0AfH6SMBx...truncated...aBcDeFgHiJ
Accept: application/json
Cache-Control: no-cache
```

**Usage:**
```bash
ffuf --request req.txt -w resource-names.txt -ac -mc 200,404 -fw 50-100 -o results.json
```

---

## Template 6: POST JSON with Auth

```http
POST /api/v1/query HTTP/1.1
Host: api.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
Accept: application/json
Content-Length: 45

{"query":"FUZZ","limit":100,"offset":0}
```

**Usage:**
```bash
ffuf --request req.txt -w sqli-payloads.txt -ac -fr "error" -o results.json
```

---

## Template 7: Multiple FUZZ Points (Custom Keywords)

```http
GET /api/v1/users/USER_ID/documents/DOC_ID HTTP/1.1
Host: api.target.com
User-Agent: Mozilla/5.0
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json
```

**Usage:**
```bash
ffuf --request req.txt \
     -w user_ids.txt:USER_ID \
     -w doc_ids.txt:DOC_ID \
     -mode pitchfork \
     -ac -mc 200 \
     -o idor_results.json
```

---

## Template 8: GraphQL Query

```http
POST /graphql HTTP/1.1
Host: api.target.com
User-Agent: GraphQL-Client/1.0
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json
Accept: application/json
Content-Length: 89

{"query":"query { user(id: \"FUZZ\") { id username email role } }","variables":{}}
```

**Usage:**
```bash
ffuf --request req.txt -w user-ids.txt -ac -mc 200 -mr '"email"' -o graphql_results.json
```

---

## How to Capture Your Own Request

### Method 1: Burp Suite
1. Intercept the authenticated request in Burp
2. Right-click → "Copy to file"
3. Save as `req.txt`
4. Edit to replace the value you want to fuzz with `FUZZ`

### Method 2: Browser DevTools
1. Open DevTools (F12) → Network tab
2. Perform the authenticated action
3. Right-click on the request → "Copy" → "Copy as cURL"
4. Convert to raw HTTP format manually
5. Insert `FUZZ` keyword where needed

### Method 3: mitmproxy
1. Run `mitmproxy` or `mitmweb`
2. Configure browser to use proxy
3. Capture the request
4. Export as raw HTTP
5. Edit to add `FUZZ` keyword

### Method 4: curl to raw request
If you have a working curl command:
```bash
# Example curl:
curl 'https://api.target.com/users/123' \
  -H 'Authorization: Bearer TOKEN'

# Convert to req.txt:
GET /users/FUZZ HTTP/1.1
Host: api.target.com
Authorization: Bearer TOKEN
```

---

## Pro Tips

1. **Content-Length**: ffuf will automatically adjust `Content-Length` header if needed
2. **Multiple FUZZ points**: Use custom keywords like `USER_ID`, `DOC_ID` with `-w wordlist.txt:KEYWORD`
3. **Testing your req.txt**: Run with a single-value wordlist first to verify it works
4. **Token expiration**: Some tokens expire quickly - have a refresh strategy ready
5. **HTTPS by default**: Use `-request-proto http` if needed for HTTP-only targets
```

## File: `ffuf-skill/resources/WORDLISTS.md`
```markdown
# FFUF Resources Reference

## Recommended Wordlists (SecLists)

### Directory/File Discovery
- **Small (Quick scans)**: `Discovery/Web-Content/common.txt` (~4.6k entries)
- **Medium**: `Discovery/Web-Content/directory-list-2.3-medium.txt` (~220k entries)
- **Large**: `Discovery/Web-Content/directory-list-2.3-big.txt` (~1.2M entries)
- **Raft Collections**:
  - `Discovery/Web-Content/raft-large-directories.txt`
  - `Discovery/Web-Content/raft-large-files.txt`
  - `Discovery/Web-Content/raft-large-words.txt`

### API Testing
- `Discovery/Web-Content/api/api-endpoints.txt`
- `Discovery/Web-Content/common-api-endpoints-mazen160.txt`
- `Discovery/Web-Content/swagger-parameters.txt`

### Subdomain Discovery
- **Top lists**:
  - `Discovery/DNS/subdomains-top1million-5000.txt`
  - `Discovery/DNS/subdomains-top1million-20000.txt`
  - `Discovery/DNS/subdomains-top1million-110000.txt`
- **Combined**: `Discovery/DNS/namelist.txt`

### Parameter Names
- `Discovery/Web-Content/burp-parameter-names.txt`
- `Discovery/Web-Content/raft-large-words.txt`

### Backup/Config Files
- `Discovery/Web-Content/backup-files-only.txt`
- `Discovery/Web-Content/Common-DB-Backups.txt`

### Authentication Testing
- **Usernames**:
  - `Usernames/top-usernames-shortlist.txt`
  - `Usernames/xato-net-10-million-usernames.txt`
- **Passwords**:
  - `Passwords/Common-Credentials/10-million-password-list-top-1000.txt`
  - `Passwords/Common-Credentials/top-20-common-SSH-passwords.txt`

### Technology-Specific
- **PHP**: `Discovery/Web-Content/PHP.fuzz.txt`
- **ASP**: `Discovery/Web-Content/IIS.fuzz.txt`
- **Apache**: `Discovery/Web-Content/Apache.fuzz.txt`
- **Git**: `Discovery/Web-Content/git-head-potential-file-exposure.txt`

## File Extensions by Technology

### PHP
`.php .php3 .php4 .php5 .phtml .phps`

### ASP/ASP.NET
`.asp .aspx .ashx .asmx .axd`

### JSP/Java
`.jsp .jspx .jsw .jsv .jspf`

### CGI/Perl
`.cgi .pl`

### Python
`.py .pyc .pyo`

### Ruby
`.rb .rhtml`

### Node.js
`.js .json`

### Backup/Interesting
`.bak .backup .old .save .tmp .swp .git .env .config .conf .log .sql .db .sqlite`

## Common Response Sizes to Filter

These are typical "not found" or default response sizes (use with `-fs`):

- **404 pages**: Often consistent sizes like 1234, 4242, 9999
- **403 Forbidden**: Check with a known forbidden path first
- **Default pages**: IIS default is often ~1433 bytes
- **Empty responses**: 0 bytes

**Tip**: Always run a test request first to identify the baseline response size, then use `-ac` to auto-calibrate!

## Useful Number Ranges for IDOR Testing

```bash
# Generate sequential IDs
seq 1 1000 > ids.txt

# Generate with padding
seq -w 0001 9999 > padded_ids.txt

# Generate UUIDs (common pattern)
# Use custom scripts or existing UUID lists
```

## Rate Limiting Guidelines

| Environment | Recommended Rate | Threads | Notes |
|-------------|-----------------|---------|-------|
| Production (careful) | `-rate 2 -t 10` | 10 | Very stealthy |
| Production (normal) | `-rate 10 -t 20` | 20 | Balanced |
| Dev/Staging | `-rate 50 -t 40` | 40 | Fast |
| Local/Testing | No limit | 100+ | Maximum speed |

## Installing SecLists

```bash
# Clone the repository
git clone https://github.com/danielmiessler/SecLists.git /opt/SecLists

# Or install via package manager (Kali)
sudo apt install seclists

# Then reference in ffuf:
ffuf -w /opt/SecLists/Discovery/Web-Content/common.txt -u https://target.com/FUZZ -ac
```

## Quick Reference: Common ffuf Patterns

### Pattern 1: Initial Directory Discovery
```bash
ffuf -w /opt/SecLists/Discovery/Web-Content/raft-large-directories.txt \
     -u https://target.com/FUZZ \
     -ac -c -v \
     -o initial_scan.json
```

### Pattern 2: Authenticated API Fuzzing
```bash
# 1. Save authenticated request to req.txt
# 2. Run:
ffuf --request req.txt \
     -w /opt/SecLists/Discovery/Web-Content/api/api-endpoints.txt \
     -ac -mc 200,201,204 \
     -o api_results.json
```

### Pattern 3: Subdomain Discovery
```bash
ffuf -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt \
     -u https://FUZZ.target.com \
     -ac -c -v
```

### Pattern 4: Parameter Discovery
```bash
ffuf -w /opt/SecLists/Discovery/Web-Content/burp-parameter-names.txt \
     -u "https://target.com/page?FUZZ=test" \
     -ac -fc 404
```

### Pattern 5: IDOR Testing (Authenticated)
```bash
# req.txt contains: GET /api/users/FUZZ/profile
ffuf --request req.txt \
     -w <(seq 1 10000) \
     -ac -mc 200 \
     -o idor_results.json
```
```

