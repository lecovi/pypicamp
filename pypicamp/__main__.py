from dotenv import load_dotenv
from .core import (
    check_internet_connection,
    check_network,
    get_network_interfaces,
    chek_internet_connection_speed,
    send_connection_status_email,
)

load_dotenv()

get_network_interfaces()

network = check_network()

if check_internet_connection():
    results = chek_internet_connection_speed()
    
    connection_status ={
        "network": network,
        "results": results,
    }
    send_connection_status_email(connection_status=connection_status)