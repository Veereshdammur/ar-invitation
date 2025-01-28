from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


def run_https_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # SSL certificate configuration
    httpd.socket = ssl.wrap_socket(
        httpd.socket, keyfile="server.key", certfile="server.cert", server_side=True
    )

    print("Serving HTTPS on 0.0.0.0 port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_https_server()
