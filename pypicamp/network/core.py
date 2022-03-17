"""
    A simple module that holds the main functions of the pypicamp package.
"""
import os
import socket

import netifaces
import requests
from rich.console import Console
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import speedtest

from pypicamp.contants import (
    INVALID_INTERFACE_PREFIX,
    IP_ADDRESS_LIST,
    HTTPS_URLS,
    DEFAULT_SOCKET_TIMEOUT,
    DEFAULT_DNS_PORT,
)


console = Console(record=True)


def send_connection_status_email(connection_status):
    html = console.export_html()

    message = Mail(
        from_email=os.environ['EMAIL_FROM_ADDRESS'],
        to_emails=os.environ['EMAIL_TO_ADDRESSES'].split(),
        subject=os.environ['EMAIL_SUBJECT'],
        html_content=html)

    sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
    response = sg.send(message)
    #FIXME: if DEBUG = True => console.log()
    console.log(connection_status, response.status_code, response.body, response.headers)


def chek_internet_connection_speed(servers=[], threads=None):
    """ Checks the internet connection speed."""
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()
    #FIXME: if DEBUG = True => console.log()
    console.log(f"Speedtest: {results_dict}")

    return results_dict


def check_internet_connection():
    """ Checks if the current computer is connected to the internet."""
    if can_access_with_url():
        #FIXME: if DEBUG = True => console.log()
        console.log(f":world_map: [bold green]The computer is connected to the internet.[/] :thumbs_up:")
        return True
    elif can_access_with_ip():
        #FIXME: if DEBUG = True => console.log()
        console.log(f"The computer is connected to the internet but [red]with DNS problems.[/]")
        return True
    else:
        #FIXME: if DEBUG = True => console.log()
        console.log(f"The computer is not connected to the internet.")
        return False


def can_access_with_url(urls=HTTPS_URLS):
    """ Checks if the current computer is connected to the internet using URL."""
    try:
        for server in urls:
            requests.get(server)
            break
    except requests.exceptions.ConnectionError:
        return False
    return True

def can_access_with_ip(ips=IP_ADDRESS_LIST):
    """ 
        Checks if the current computer is connected to the internet using IP addresses.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setdefaulttimeout(DEFAULT_SOCKET_TIMEOUT)
    try:
        for ip in ips:
            s.connect((ip, DEFAULT_DNS_PORT))
    except socket.error:
        return False
    return True


def network_status():
    """ Checks if the current computer is connected to a network."""
    hostname = socket.gethostname()
    interfaces = get_network_interfaces()
    ip_addresses = []
    for iface in interfaces:
        addr = netifaces.ifaddresses(iface)
        #FIXME: if DEBUG = True => console.log()
        console.log(f"Interface LINK: {addr[netifaces.AF_LINK]}")
        console.log(f"Interface IPv4: {addr[netifaces.AF_INET]}")
        ip_addresses.append(addr[netifaces.AF_INET][0]["addr"])
        #FIXME: if DEBUG = True => console.log()
        console.log(f"Interface IPv6: {addr[netifaces.AF_INET6]}")
    #FIXME: if DEBUG = True => console.log()
    console.log(f"Your Computer Name is: [bold]{hostname}[/] @ {ip_addresses}")

    network = {
        "hostname": hostname,
        "interfaces": interfaces,
    }
    return network


def get_network_interfaces():
    """ Gets the network interfaces of the current computer."""
    interfaces = netifaces.interfaces()
    #FIXME: if DEBUG = True => console.log()
    console.log(f"Interfaces: {interfaces}")
    valid_interfaces = __removes_invalid_interfaces(interfaces)
    #FIXME: if DEBUG = True => console.log()
    console.log(f"Available interfaces: {valid_interfaces}")
    return valid_interfaces


def __removes_invalid_interfaces(interfaces):
    """ Removes invalid interfaces from the list of interfaces."""
    valid_interfaces = []
    for iface in interfaces:
        #FIXME: if DEBUG = True => console.log()
        console.log(f"Checking interface: {iface}")
        if iface.startswith(INVALID_INTERFACE_PREFIX):
            #FIXME: if DEBUG = True => console.log()
            console.log(f"Invalid interface: {iface}")
        else:
            valid_interfaces.append(iface)
    return valid_interfaces