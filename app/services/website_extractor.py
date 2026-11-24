from urllib.parse import urljoin
import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException
from app.utils.validators import validate_url

def extract(url):
    # Pin the checked address, preserving the original Host and TLS hostname.
    try:
        with httpx.Client(timeout=10,follow_redirects=False,trust_env=False) as client:
            for _ in range(4):
                p, ip, port = validate_url(url)
                target = httpx.URL(url).copy_with(host=ip)
                with client.stream('GET',target,headers={'Host':p.netloc,'User-Agent':'AssignmentWebsiteAnalyzer/1.0','Accept':'text/html'},extensions={'sni_hostname':p.hostname}) as res:
                    if res.status_code in (301,302,303,307,308):
                        url=urljoin(url,res.headers['location']); continue
                    res.raise_for_status()
                    if 'text/html' not in res.headers.get('content-type','').lower():
                        raise HTTPException(422,'Website must return HTML')
                    raw=bytearray()
                    for chunk in res.iter_bytes(chunk_size=8192):
                        raw.extend(chunk)
                        if len(raw)>1_000_000:
                            raise HTTPException(413,'Website exceeds size limit')
                    break
            else:
                raise HTTPException(422,'Too many redirects')
    except (httpx.HTTPError,KeyError) as exc:
        raise HTTPException(502,'Website inaccessible') from exc
    soup=BeautifulSoup(bytes(raw),'html.parser')
    title=soup.title.get_text(' ',strip=True) if soup.title else ''
    meta=soup.find('meta',attrs={'name':'description'})
    for tag in soup(['script','style','noscript','svg','nav','footer','header']): tag.decompose()
    lines=list(dict.fromkeys(s.strip() for s in soup.stripped_strings if s.strip()))
    text='\n'.join(lines)[:16000]
    if len(text)<80: raise HTTPException(422,'Insufficient readable content; JavaScript-only pages are not supported')
    return {'url':url,'title':title,'description':meta.get('content','') if meta else '', 'text':text}
