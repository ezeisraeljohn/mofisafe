
# Mofisafe  - A Financial Tracking App

Welcome to The Mofisafe App. This is a Django application designed to help you manage your finances.

You can visit the deployed site here. For more insights and detailed information, check out the final project blog article here.




## Acknowledgements

 - [Tailwind Official Documentation](https://v2.tailwindcss.com/docs)
 - [Django Official Documentation](https://docs.djangoproject.com/en/5.0/)


## API Reference

#### To access the Mofisafe API, use the following endpoint. This will take you to our Django REST Framework (DRF) home page, where you can view and interact with all available API endpoints once logged in.

```http
  GET /api/v1/
```

## Authentication. 

#### Access to the API requires authentication. Ensure that you are logged in to access the full range of API endpoints. You must sign up as a user to login via the DRF hime page

```http
  GET api/v1/auth/
```


## Authors

- [@Ughagwu Oluchukwu](https://github.com/oluchristian)
- [@Eze Israel John](https://github.com/ezeisraeljohn)
- [@Sanele Skhosana](https://github.com/sanzamcmillian)


## Installation

To get a local copy up and running, follow these simple steps.

```bash
  git clone https://github.com/ezeisraeljohn/mofisafe.git
  cd mofisafe
```

Create a virtual environment.

```bash
  python -m venv venv
```

Activate the virtual environment.

```bash
  source venv/bin/activate
```

Install dependencies.

```bash
  pip install -r requirements.txt
```

Apply migrations

```bash
  python manage.py migrate
```

Apply migrations

```bash
  python manage.py migrate
```

Run the development server

```bash
  python manage.py runserver
```
    
## Usage/Examples

Once the server is running, you can access the application in your web browser at http://127.0.0.1:8000/.


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request

