> # DataShell21 - Advanced HTTP Server Toolkit

A comprehensive command-line toolkit for server interaction, data posting, and network diagnostics with multi-protocol support and real-time monitoring capabilities.

> ## Overview

DataShell21 is a powerful Python-based toolkit designed for server administrators, developers, and security professionals. It provides a unified interface for performing various HTTP operations, server diagnostics, and data management tasks through a modular command system.

> ## Features

- **Multi-protocol HTTP Operations**: Support for GET, POST, PUT, DELETE, HEAD, and OPTIONS requests
- **Server Diagnostics**: Ping testing, server information retrieval, and connection monitoring
- **Data Management**: JSON data posting with automatic file handling
- **Custom Headers Support**: Flexible header configuration for advanced HTTP requests
- **Comprehensive Logging**: Detailed response logging with JSON parsing
- **Modular Architecture**: Separated components for easy maintenance and extension
- **Real-time Monitoring**: Live connection tracking and status reporting

> ## Installation

> ### Requirements
- Python 3.6 or higher
- Required libraries

> ### Setup
```bash
# Install required packages
pip install requests
```

> ## Project Structure

```
datashell21/
├── _Starter.py                    # Main launcher script
├── main\_main_file_\__data_poster__.py  # Core data posting module
├── __data_poster__.py            # Data posting functionality
├── __info_server__.py            # Server information retrieval
├── __ping_server__.py            # Server ping and connectivity testing
├── __requests_server__.py        # HTTP request handling
├── main_data_file__data__.json   # Default data configuration
└── README.md                     # Documentation
```

> ## Usage

> ### Basic Commands

```bash
# Launch the toolkit
python _Starter.py [options]

# Post data to server
python _Starter.py -url "http://example.com/api" -data

# Get server information
python _Starter.py -url "http://example.com" -info

# Ping server
python _Starter.py -url "http://example.com" -ping

# Send custom HTTP request
python _Starter.py -url "http://example.com/api" -request GET
```

> ### Advanced Usage

```bash
# Post data with custom headers
python _Starter.py -url "http://example.com/api" -data -H "Authorization: Bearer token" -H "Content-Type: application/json"

# Send POST request with JSON data
python _Starter.py -url "http://example.com/api" -request POST -data

# Ping server from specific module
python __ping_server__.py -url "http://example.com"

# Direct module usage
python __info_server__.py -url "http://example.com"
python __requests_server__.py -url "http://example.com/api" -method GET
```

> ### Command Line Options

```
-url, --url        Server URL (required)
-data, --data      Post data from JSON file to server
-info, --info      Get server information and headers
-ping, --ping      Ping server and test connectivity
-request, --request  Send custom HTTP request (GET, POST, PUT, DELETE, HEAD, OPTIONS)
-H, --header       Custom headers in 'Header-Name: value' format
-method, --method  HTTP method for custom requests
```

> ## Data Configuration

The toolkit uses a JSON configuration file (`main_data_file__data__.json`) for data posting:

```json
{
  "app": "datashell21",
  "version": "1.0.0",
  "timestamp": "2024-01-01T12:00:00Z",
  "data": {
    "user_id": 1001,
    "username": "test_user",
    "status": "active"
  },
  "settings": {
    "auto_save": true,
    "log_level": "info"
  }
}
```

> ## Response Format

All responses include:
- HTTP status code
- Response headers
- Response body (JSON or text)
- Execution time
- Error handling with detailed messages

> ## Error Handling

The toolkit provides comprehensive error handling for:
- Network connectivity issues
- Invalid URLs
- JSON parsing errors
- Server timeouts
- Permission errors
- Invalid HTTP responses

> ## Examples

> ### Example 1: Server Diagnostics
```bash
# Check server status and information
python _Starter.py -url "https://api.example.com" -info
python _Starter.py -url "https://api.example.com" -ping
```

> ### Example 2: API Interaction
```bash
# Send data to REST API
python _Starter.py -url "https://api.example.com/users" -data

# Retrieve data from API
python _Starter.py -url "https://api.example.com/users/123" -request GET
```

> ### Example 3: Security Testing
```bash
# Test server headers
python _Starter.py -url "https://target.com" -info

# Check server responsiveness
python _Starter.py -url "https://target.com" -ping
```

> ## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

> ## License

This project is licensed under the MIT License - see the LICENSE file for details.

> ## Support

For support, questions, or feature requests:
- Open an issue in the GitHub repository
- Check the documentation for troubleshooting
- Review existing issues for similar problems

> ## Version History

1.0.0 - Initial release with core functionality
- HTTP request handling
- Server diagnostics
- Data posting capabilities
- Modular architecture
