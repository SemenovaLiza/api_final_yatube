# api_final_yatube
### *Description*
api_final_youtube project is an API for the Yatube social network. With the help of the project, authorized users can change data about objects created by them, and unauthorized users can get information about these objects.

### *Technologies*
- Python 3.7
- Django 3.2.16
- django rest framework 3.12.4
- django rest framework-simplejwt 4.7.2
#### *The rest of the technologies can be found in the requirements.txt file*

### *Project features*
- Getting, creating, updating, deleting posts.
- Getting group's information.
- Getting, creating, updating, deleting comments.
- Getting, creating user's following.

[Project documentation](http://127.0.0.1:8000/redoc/)
###### link will open after the project is deployed
### *How to launch a project*
Using terminal change the current working directory to the location where you want the cloned directory.

Clone the repository and go to it:
```
git clone git@github.com:SemenovaLiza/api_yatube.git
```
```
cd api_yatube
```
Install and activate the virtual environment:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Install dependencies from the file requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
A token is required to use some methods in the in api_yatube project. If you already have an Yatube account, log in via the request:
```
api/v1/jwt/create/
```
You will receive a token in the 'access' field that will be passed in the header of each request, in the "Authorization" field. 

Example:
```
Bearer #########
```
### *Examples of requests using API in api_yatube:*

### Posts requests
#### POST request api/v1/posts/
```
{
    "text": ""string",
    "group": 3
} 
```
#### GET request api/v1/posts/{post_id}/
```
{
  "id": 1,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 3
}
```
#### PUT request api/v1/posts/{post_id}/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
### Group request
#### GET request api/v1/groups/3/
```
{
  "id": 3,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
### Comments requests
#### POST api/v1/posts/{post_id}/comments/
```
{
  "text": "string"
}
```
#### GET api/v1/posts/{post_id}/comments/{comment_id}/
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
#### PUT request api/v1/posts/{post_id}/comments/{comment_id}/
```
{
  "text": "string"
}
```
### Follow requests
#### GET api/v1/follow/
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```
#### POST api/v1/follow/
```
{
  "following": "string"
}
```
### Author
Semenova Elizaveta
