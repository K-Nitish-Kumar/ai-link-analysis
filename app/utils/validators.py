import ipaddress, socket
from urllib.parse import urlsplit
from fastapi import HTTPException

def validate_url(url):
    try:
        p = urlsplit(url)
        if p.scheme not in ('http','https') or not p.hostname or p.username or p.password:
            raise ValueError()
        port = p.port or (443 if p.scheme=='https' else 80)
        if port != (443 if p.scheme=='https' else 80):
            raise ValueError()
        addresses = {x[4][0] for x in socket.getaddrinfo(p.hostname,port,type=socket.SOCK_STREAM)}
        if not addresses or any(not ipaddress.ip_address(a).is_global or ipaddress.ip_address(a).is_multicast for a in addresses):
            raise ValueError()
        return p, sorted(addresses)[0], port
    except (ValueError,OSError) as exc:
        raise HTTPException(400,'Only reachable public HTTP(S) websites on standard ports are allowed') from exc
