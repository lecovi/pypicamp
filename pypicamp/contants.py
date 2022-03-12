DEFAULT_SOCKET_TIMEOUT = 3
DEFAULT_DNS_PORT = 53

IP_ADDRESS_LIST = (
    "1.1.1.1",         # Cloudflare
    "1.0.0.1",
    "8.8.8.8",         # Google DNS
    "8.8.4.4",
    "208.67.222.222",  # Open DNS
    "208.67.220.220",
)

HTTPS_URLS = (
    "https://google.com",
    "https://facebook.com",
    "https://youtube.com",
    "https://twitter.com",
    "https://wikipedia.org",
    "https://amazon.com",
    "https://mercadolibre.com.ar",
)

INVALID_INTERFACE_PREFIX = (
    "lo",      # Loopback interface
    "docker",  # Docker interface
    "br-",     # Bridge interface
    "virbr",   # Virtual bridge interface
)
