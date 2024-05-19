# Clerk Django

"Clerk Django" is a Python library that offers middleware and permissions for authenticating requests when your authentication process is managed by Clerk.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install clerk_django.

```bash
pip install clerk-django
```

## Usage

The first step will be to set your `CLERK_SECRET_KEY` and `CLERK_PEM_PUBLIC_KEY` in your environment variables.
Then go to your `settings.py` file and set the `ALLOWED_PARTIES` config.

```python
ALLOWED_PARTIES = ["http://localhost:5173"]
```

To use the `ClerkAuthMiddleware`, add `clerk_django.middlewares.clerk.ClerkAuthMiddleware` to your middlewares.

```python
MIDDLEWARE = [
    # other middlewares
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'clerk_django.middlewares.clerk.ClerkAuthMiddleware'
]
```

Once you have added the middleware, you can access the user from the request using `request.clerk_user`. clerk_user has 3 properties.

- `is_authenticated` - It is true/false based on if the user is authenticated or not.
- `id` - Clerk user id. This key will be available only if the user is authenticated.
- `decoded_token` - This is the value after decoding the token which might contain useful user info based on how you have configured your [JWTTemplates in Clerk](https://clerk.com/docs/backend-requests/making/jwt-templates). This key will be available only if the user is authenticated.

```python
from rest_framework import viewsets
from rest_framework.response import Response
from permissions.clerk import ClerkAuthenticated

class ExampleViewset(viewsets.ViewSet):
    permission_classes = [ClerkAuthenticated]

    def list(self, request):
        user_id = request.clerk_user.get('id')
        return Response()
```

There is a wrapper around the User related apis. All the different function can be found in [clerk backend sdk](https://clerk.com/docs/references/backend/user/get-user-list) and [ clerk backend apis ](https://clerk.com/docs/reference/backend-api/tag/Users#operation/GetUserList)

```python
from clerk_django.client import ClerkClient

#Set your CLERK_SECRET_KEY and CLERK_PEM_PUBLIC_KEY in your environment variables.

cc = ClerkClient()

user_details = cc.users.getUser(user_id=user_id)

#Check the clerk documentation for the list of query params.
user_list = cc.users.getUserList({
               "email_address" : ["reachsahilverma@gmail.com"]
            })
```

I have added all the functions mentioned in the [Clerk Backend SDK - User](https://clerk.com/docs/references/backend/user/get-user-list). You just need to use `user_id` instead of `userId`. Also in case of `verifyPassword`, just pass the `user_id` and `password` directly. In all the other functions you can pass the params as required and mentioned in the documentation.

```python
res = cc.users.verifyPassword(user_id,password)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://github.com/ravikrsngh/clerk_django?tab=MIT-1-ov-file)
