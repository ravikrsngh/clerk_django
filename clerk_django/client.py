import os
import jwt
import requests
from . import resources

class ClerkClient:
    api_key: str
    public_pem_key: str
    users: resources.UserResource
    base_url: str = "https://api.clerk.com/v1"

    def __init__(self, api_key: str | None=None, public_pem_key: str | None=None) -> None:
        if api_key is None:
            api_key = os.environ.get("CLERK_SECRET_KEY")
        if api_key is None:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the CLERK_SECRET_KEY environment variable"
            )
        self.api_key = api_key
        
        if public_pem_key is None:
            public_pem_key = os.environ.get("CLERK_PEM_PUBLIC_KEY")
        self.public_pem_key = public_pem_key
        
        self.users = resources.UserResource(self)

    
    def decode_jwt(self, token: str):
        if self.public_pem_key:
            return jwt.decode(token, key=self.public_pem_key, algorithms=['RS256', ])
        else: 
            raise Exception(
                "The public_pem_key client option must be set either by passing public_pem_key to the client or by setting the CLERK_PEM_PUBLIC_KEY environment variable"
            )
    
    def get(self,url, params={}):
        res = requests.get(url=f'{self.base_url}/{url}',params=params, headers={
            'Authorization': f'Bearer {self.api_key}'
        })
        print(res.url)
        return res

    def post(self,url, data={}):
        res = requests.post(url=f'{self.base_url}/{url}',data=data, headers={
            'Authorization': f'Bearer {self.api_key}'
        })
        print(res.url)
        return res
    
    def patch(self,url, data={}):
        res = requests.patch(url=f'{self.base_url}/{url}',data=data, headers={
            'Authorization': f'Bearer {self.api_key}'
        })
        print(res.url)
        return res
    
    def delete(self,url):
        res = requests.delete(url=f'{self.base_url}/{url}', headers={
            'Authorization': f'Bearer {self.api_key}'
        })
        print(res.url)
        return res

