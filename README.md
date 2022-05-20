# heroku-demo
Creating CI/CD Pipeline using GitHub Actions for Python Project (Heroku Deployment Example)

## Prerequisite
### Sign up 
https://www.heroku.com/

### install heroku CLI
~~~
brew install heroku/brew/heroku

heroku login

heroku create py-heroku-demo
# When you create an app, a git remote (called heroku) is also created and associated with your local git repository.
# https://py-heroku-demo.herokuapp.com/ | https://git.heroku.com/py-heroku-demo.git


heroku authorizations:create 

Creating OAuth Authorization... done
Client:      <none>
ID:          xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
Description: Long-lived user authorization
Scope:       global
Token:       xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
Updated at:  Fri May 20 2022 12:45:01 GMT+0700 (Indochina Time) (less than a minute ago)
