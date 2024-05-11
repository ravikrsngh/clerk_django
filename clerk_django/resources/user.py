
class UserResource:
    base_url: str = 'users'

    def __init__(self, client) -> None:
        self._client = client
    
    def getUser(self, user_id):
        return self._client.get(f'{self.base_url}/{user_id}')
    
    def getUserList(self, params):
        return self._client.get(f'{self.base_url}', params=params)

    def getCount(self, params):
        return self._client.get(f'{self.base_url}/count', params=params)
    
    def getOrganizationMembershipList(self, user_id, params={}):
        return self._client.get(f'{self.base_url}/{user_id}/organization_memberships', params=params)
    
    def getUserOauthAccessToken(self, user_id, provider):
        return self._client.get(f'{self.base_url}/{user_id}/oauth_access_tokens/{provider}')
    
    def createUser(self, data={}):
        return self._client.post(f'{self.base_url}', data=data)
    
    def verifyPassword(self, user_id, password):
        return self._client.post(f'{self.base_url}/{user_id}/verify_password', data={"password":password})
    
    def banUser(self, user_id):
        return self._client.post(f'{self.base_url}/{user_id}/ban')
    
    def unbanUser(self, user_id):
        return self._client.post(f'{self.base_url}/{user_id}/unban')
    
    def lockUser(self, user_id):
        return self._client.post(f'{self.base_url}/{user_id}/lock')
    
    def lockUser(self, user_id):
        return self._client.post(f'{self.base_url}/{user_id}/unlock')
    
    def updateUser(self, data={}):
        return self._client.patch(f'{self.base_url}', data=data)
    
    def updateUserMetadata(self,user_id, data={}):
        return self._client.patch(f'{self.base_url}/{user_id}/metadata', data=data)
    
    def deleteUser(self, user_id):
        return self._client.delete(f'{self.base_url}/{user_id}')
    
    def disableUserMFA(self, user_id):
        return self._client.delete(f'{self.base_url}/{user_id}/mfa')