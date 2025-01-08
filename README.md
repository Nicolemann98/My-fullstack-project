# Coder's Cafe 
This is a fullstack project written in Python using the Django framework on the backend, connecting to a PostgreSQL database. Using the bootstrap framework on the frontend within HTML and CSS.

## Plan & Design Process
I have detailed my planned features within User Stories, which can be found at: https://github.com/users/Nicolemann98/projects/1/views/1

The aim was to make a site that would be accessible and easy to navigate - the colour scheme adding a good contrast. All relevant features for this project have been inclued in the above link with bulletpoint analysis.

Link to Figma design process: https://www.figma.com/design/wKYgnjRE7IqIvDQStcXiWu/Untitled?node-id=0-1&t=2rsoia2qxCDk3lRP-1

## Important notes 
The staff user that can view all of the bookings on the booking screen is as follows, username: `staff.member` & password is: `Password11*`.

In order to test the functions of the bookings page and all its features, new users can be created in the account page.

## Testing
Initally I tested to ensure that the homepage would be responsive over desktop, tablet and mobile screens
Responsive home screen on mobile:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/384ffaa3-721a-4104-b30e-7fe7d9bfc96c)

Responsive homescreen on tablet: 

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/bcc60b0f-dcb3-4cd0-b1b5-34c85b6a1c77)

This is the booking screen from the staff member's perspective:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/cab76240-db4b-4a14-8019-cc8108eda2d5)

This is the account page: 

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/a29c9a00-804c-4b65-8172-b6840cb4f2b6)

This is the menu page:

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/3dcfaa3c-8e05-496e-ab07-3860b32ff5fe)

Upon clicking the download button on the menu page, users will have the option to download a pdf version of the menu

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e3207977-0aaf-4725-85a3-09f84d018f52)


Now we will start testing the booking functionality. Logging in as JohnDoe, we can see that he has no bookings

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e3516df0-a2b6-414a-b930-d041a36044d4)

We will click create booking and fill in the form

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/9f99628c-3fec-47e7-a5ca-3a7a5e0bcd8d)

Upon clicking submit, we can see that this booking has been added, along with a confirmation message

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/edf28df4-73ff-464b-a768-675c900f1f03)

The cafe has a total of 20 seats, now we will try to create the following booking that will exceed the cafe's capacity

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b4a9ac5e-c28a-4b5e-8db9-f298f7f75601)

Clicking submit, we are given an error message telling us there aren't enough seats

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/1028da96-0159-4123-98bc-2e5a8c1d2234)

And the booking has not been saved

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e182766f-0318-4a7d-b215-9ae3076b4b1d)

Similarly if we try to create a booking in the past

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/7c17e097-be30-4282-8187-ff10fdca3239)

Finally if we click delete on the booking, we get a warning message

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/0ee45471-a26f-4459-8661-87aedd60b8ff)

And we see that if we click delete on the pop-up to confirm, the booking is deleted

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/700a419a-b00a-474c-afa8-174bda604db8)



## Bugs 

There was a bug, that when editing a booking, the validation for number of seats failed because the validator got all the bookings with the same start time,
summed their number of seats and added the number of seats of the new booking, however this failed because if you didn't change the start time of the booking you are editing,
then that booking got counted twice. I fixed this by adding a filter to the bookings we received to not include the previous booking which was amended.

### Python Validator

The code passes the Code Institure Linter Python Validation with zero errors.

forms.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/8fb0594c-a0d1-4ed4-95f4-121383d3775c)

models.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/0757cb68-5fe3-400e-8a9e-6b4e90f12d53)

test_forms.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b216e4c2-e08b-4757-bb32-63aee0f5f6dc)

test_views.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/b5ca207b-34be-4e66-9a07-b5ab58365489)

urls.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/e934a848-1d71-46ca-9327-13b3b2286a55)

views.py

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/f7c2bc0f-6a94-4c9b-9492-910c34e23b3c)


### HTML W3C Validator

Index Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/5e189f2a-8c12-40aa-a08b-0987f0def4e0)

Menu Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/7782b4f2-7a30-4554-91eb-8926ab2f3dcc)

Account Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/45fd9387-1328-4183-96a3-5bf979b60b97)

Bookings Page

![image](https://github.com/Nicolemann98/My-fullstack-project/assets/144236128/17d11e11-6abc-4658-adde-b318d5a702e8)

The only pages that fail the validations are the ones using the Django forms (which can delibarately fail them for performance reasons). For example the signup screen [fails the validation](https://validator.w3.org/nu/?doc=https://nicole-full-stack-project-7589e5b487d3.herokuapp.com/accounts/signup/). But looking into the error, we can see that this code is not in my project, but auto-generated from Django forms so can be ignored.

![image](https://github.com/user-attachments/assets/40cd3a6b-253a-46b7-bf98-d72a9f648d03)


## Deployment 

This project was deployed onto Heroku, the link for which is: https://nicole-full-stack-project-7589e5b487d3.herokuapp.com/

Automatic deployments are enabled through Heroku. To deploy, simply git commit and push to the main branch. If however you want to host it yourself follow the following instructions. Note that I am assuming that you have a GitHub account, git bash installed with it linked to your GitHub account, and a Heroku account with linked to your GitHub account. If that is not the case, do that now. If you do not have the links to your GitHub account, you can follow these steps and link accounts when prompted by git bash and Heroku.

### Cloning repository to local GitHub account

First start by cloning this repository into your local GitHub account using the following steps. [See the GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository)), my steps are a copy provided in that documentation, with a few minor tweaks to make them specific to this repo.

1. Open git bash in a desired location on your desktop
2. Create a bare clone of this repository
   ```
   git clone --bare https://github.com/Nicolemann98/My-fullstack-project.git
   ```
4. Open your GitHub account and create a new, blank repository, this should provide a link to use in the next step
   ![image](https://github.com/user-attachments/assets/19f3d414-35c3-47ef-92a3-1851ae43f560)
5. Mirror-push your clone to the newly created repository, replacing the link with the link copied in the previous step
   ```
   cd My-fullstack-project.git
   git push --mirror https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git
   ```
6. Remove the temporary local repository you created earlier
   ```
   cd ..
   rm -rf My-fullstack-project.git/
   ```

Now you should have a version of this repository within your GitHub account.
![image](https://github.com/user-attachments/assets/aed83c1b-b9f0-495e-8381-1fbe586b64e3)

### Setting up database

If you are going to use this for more than testing purposes, I would recommend finding a database hosting service that you like. For this I originally used ElephantSQL.com which is now discontinued, however there are many more options online and I will give steps to set up SQLite with this project. In both cases, follow the steps below.

1. Clone your repository (not this one, but the dupicate that you created previously) locally. I used gitpod for this, by linking my GitHub account there was no need for any commands, just choosing the correct repo. However you can use your favourite IDE along with git if you'd prefer.
2. Install all the dependencies, I have frozen them in [requirements.txt](requirements.txt) so just run
   ```
   pip3 install requirements.txt
   ```
3. If you are using your own database hosting service skip to step 7.
4. Open [settings.py](settings.py)
5. Change the line with SECRET_KEY on to
   ```
   SECRET_KEY = os.environ.get("SECRET_KEY")
   ```
6. Find the databases section of settings, add and remove the comments to make it equal to this
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
   }
   
   # DATABASES = {
   #     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
   # }
   
   if 'test' in sys.argv:
       DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
   
   # del DATABASES['default']['OPTIONS']['sslmode']
   ```
7. If you are hosting your own database resume here
8. Create a superuser for the application, ensuring to choose a sensible username and password that you will remember for this user
   ```
   python manage.py createsuperuser
   ```
9. Migrate the database - note this does not transfer any data, only the metadata about tables, fields etc
   ```
   python3 manage.py migrate
   ```
10. Push these changes to GitHub
    ```
    git add .
    git commit -m "Change database setup to use SQLite"
    git push
    ```

### Deploying to Heroku

Finally, it is time to deploy to Heroku. Use the following steps to deploy your clone to Heroku (note that Heroku may change their deployment process leading these steps to be out of date). There are other ways to do this using the Heroku CLI, if you are more comfortable with that, then feel free, however I will rely on the web application as much as possible for ease.

1. Go to https://dashboard.heroku.com/
2. Click `New` then `Create new app`
3. Name your application, select the applicable region, and click `Create app`
   ![image](https://github.com/user-attachments/assets/24ff3524-bad4-404a-94eb-1e09ec7cd6f0)
4. Under `Deployment Method` select GitHub, enter the cloned repository's GitHub account and location below and press search
   ![image](https://github.com/user-attachments/assets/16f70636-7bc5-41ab-ba8c-03435cbd88a6)
5. The repository clone should appear, click `connect`.  You should be redirected to the deployment page.
6. Go to the settings page, click `Reveal Config Vars`, and add a new one with the key as `DISABLE_COLLECTSTATIC` and value as `1`.
7. Connect the database, if you are hosting your own, follow step (i), otherwise if you followed my steps to use SQLite, follow step (ii)
    1. Find the database URL within your host and add a new config var `DATABASE_URL` that has the URL as it's value. Also if there are any other steps in your chosen host's documentation, then follow them too.
    2. Go to https://djecrety.ir/ to create a django secret key, copy it and create a new config var `SECRET_KEY` and paste your new secret key as the value
8. Go to the deployment page, scroll down, depending on whether you want a single deployment or auto deployments either click `Deploy Branch` or `Enable Automatic Deploys`
   ![image](https://github.com/user-attachments/assets/b3697a0f-423f-443f-a17a-b04b4f104559)
9. Once it has finished running, at the top, click `Open app`
   ![image](https://github.com/user-attachments/assets/ffc00331-2574-42bc-9bec-34a0d4b93adb)

Once you have done all of that, you should be directed to the page where you have hosted this project. Note that none of the data from this project will be transferred over as you will be using your own database so it will be a blank slate. The only registered user will be the admin one created within the database steps.

## Credits 

- Code institute course materials
- Django documentation: https://docs.djangoproject.com/en/5.0/
- Font Awesome for icons
- Favicon created from https://favicon.io/favicon-converter/
- Photos used on main page are from:
    https://blog.hyperiondev.com/index.php/2018/08/06/what-kind-of-companies-do-coders-work-for/  (coder's photo)
    https://www.chinadaily.com.cn/bizchina/tech/2016-03/09/content_23789709.htm (mock cafe photo)
- Photo of scone on menu page from Pexels

## Struggles

This project was very challenging in a number of ways, not only as it was my first ever fullstack project, but also because there was
a large number of new materials to also learn in addition to changing my existing skills to adapt to the additon of Bootstrap and Django.

There were a numnber of issues with deployment which needed to be amended to fix the functionality of the bookings and account pages, and also a number of differences in the styling upon deployment.

I received terminal errors when trying to run unit tests, regarding not being able to connect to the database, after searching online forums for help, I found that adding the following line under the databases section of the settings.py file 

```del DATABASES['default']['OPTIONS']['sslmode']```








