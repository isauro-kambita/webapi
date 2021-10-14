# webapi
This is my first django api

## Chapter 1

**Welcome to chapter 1**


Code example

```
def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )

```
