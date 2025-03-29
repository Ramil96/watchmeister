# Deployment Guide for Watchmeister

This guide provides detailed steps to deploy the Watchmeister project, which is built using Django and hosted on Heroku. The project utilises Amazon S3 for static files, a PostgreSQL database provided by Code Institute for students, and Stripe for payment processing. The development environment is managed using GitPod and GitHub.

## Prerequisites

Ensure you have the following prerequisites installed and set up:

- A GitHub account
- A Heroku account
- Git installed on your local machine
- An Amazon S3 bucket for static and media files
- A PostgreSQL database
- A Stripe account for payment processing
- GitPod workspace (optional but recommended for development)

## Step 1: Clone the Repository

First, clone the Watchmeister repository from GitHub to your local machine:

```sh
git clone https://github.com/yourusername/watchmeister.git
cd watchmeister
```

## Step 2: Set Up Environment Variables

Create a file named `.env` in the root directory of the project and add the following environment variables:

```sh
# Database
DATABASE_URL=your_postgresql_url

# Django settings
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=your_heroku_app_url,localhost,127.0.0.1

# AWS S3 settings
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name

# Stripe settings
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WH_SECRET=your_stripe_webhook_secret  # Webhook secret key

# Email settings (for order confirmations)
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
```

Replace each placeholder with the actual values from your environment. Make sure to keep the `.env` file secure and do not share it publicly.

### Adding `.env` to `.gitignore`

To ensure that your sensitive environment variables are not tracked by Git, add `.env` to your `.gitignore` file:

1. Open or create a file named `.gitignore` in the root directory of your project.
2. Add the following line to `.gitignore`:
   ```sh
   .env
   ```
3. Save and close the `.gitignore` file.

## Step 3: Set Up Amazon S3 Bucket

1. **Create an Amazon S3 Account:** Sign up or log in to your Amazon Web Services (AWS) account.
2. **Create a Bucket:** Create an S3 bucket for your static and media files.
3. **Bucket Permissions:** Set up the appropriate permissions to allow public access to your static files.
4. **Update Environment Variables:** Add your `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_STORAGE_BUCKET_NAME` to your `.env` file.

For more details, refer to the [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

## Step 4: Set Up GitPod (Optional)

To develop using GitPod, you can open your repository in GitPod using the following link:

```
gitpod.io/#https://github.com/yourusername/watchmeister
```

Alternatively, you can use VS Code or any other IDE for local development.

## Step 5: Install Dependencies

Install the required Python packages using pip:

```sh
pip install -r requirements.txt
```

## Step 6: Set Up Stripe Payment System

Stripe is used to process payments in Watchmeister. To integrate Stripe, follow these steps:

1. **Create a Stripe Account:** Sign up for an account on [Stripe](https://stripe.com).
2. **Create API Keys:** Obtain your `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` from the Stripe dashboard.
3. **Set Up Webhooks:** Create a webhook in Stripe to listen for events like successful payments and order completions. Note the `STRIPE_WH_SECRET` value.
4. **Add Keys to Environment Variables:** Include `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, and `STRIPE_WH_SECRET` in your `.env` file.

For more information on integrating Stripe, refer to the [Stripe Documentation](https://stripe.com/docs).

## Step 7: Run the Application Locally

To test the application locally, run the Django development server:

```sh
python manage.py runserver
```

The application should now be running at [http://localhost:8000](http://localhost:8000).

## Step 8: Prepare for Heroku Deployment

### Update `requirements.txt`
Ensure your `requirements.txt` is up to date by running:

```sh
pip freeze > requirements.txt
```

### Create `Procfile`
Create a `Procfile` in the root directory with the following content:

```sh
web: gunicorn watchmeister.wsgi
```

## Step 9: Deploy to Heroku

### Login to Heroku and Create a New Application

```sh
heroku login
heroku create watchmeister
```

### Set Up Environment Variables on Heroku

Use the following commands to set your environment variables on Heroku:

```sh
heroku config:set DATABASE_URL=your_postgresql_url
heroku config:set SECRET_KEY=your_secret_key
heroku config:set AWS_ACCESS_KEY_ID=your_aws_access_key_id
heroku config:set AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
heroku config:set AWS_STORAGE_BUCKET_NAME=your_bucket_name
heroku config:set STRIPE_PUBLIC_KEY=your_stripe_public_key
heroku config:set STRIPE_SECRET_KEY=your_stripe_secret_key
heroku config:set STRIPE_WH_SECRET=your_stripe_webhook_secret
heroku config:set EMAIL_HOST_USER=your_email
heroku config:set EMAIL_HOST_PASSWORD=your_email_password
```

Replace the placeholder values with the actual credentials.

## Step 10: Push to Heroku

Initialise a Git repository (if not already done), add Heroku remote, and deploy:

```sh
git init
heroku git:remote -a watchmeister
git add .
git commit -m "Initial commit"
git push heroku main
```

## Step 11: Access Your Application

After deploying, you can access your application at your Heroku app URL, which will look something like:

```
https://watchmeister.herokuapp.com/
```

## Conclusion

You have successfully deployed the watchmeister project to Heroku. For any changes, commit them to your GitHub repository and push to Heroku to update your application.

For further customisation or issues, refer to the following documentation:

- [Heroku Django Documentation](https://devcenter.heroku.com/articles/django-app-configuration)
- [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Project Documentation](https://djangoproject.com/)
- [Stripe Documentation](https://stripe.com/docs)

*Happy coding!*