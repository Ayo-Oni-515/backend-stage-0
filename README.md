# stage-0-backend
*HNG 13 backend track stage 0*

A publicly accesible RESTful API that returns my profile information along with a dynamic cat fact fetched from an external API. Implementation was achieved using python's FastAPI framework


## Local Setup
1. Clone the repository

        git clone https://github.com/Ayo-Oni-515/backend-stage-0.git

2. Create a virtual environment

        python -m venv <environment-name>

3. Activate the virtual environment

        source <environment-name>/Script/activate (on windows)

        source <environment-name>/bin/activate (on linux and Mac)

4. Install dependencies

    Dependencies are available in requirements.txt

    * fastapi[standard]
    * requests

    To install dependencies on local machine

        pip install -r requirements.txt

3. Test locally by using this command then click on the localhst link provided in the terminal.

        fastapi run

## API Documentation
To access online, use endpoint URL:

    https://

Typical JSON Response Format (200 OK):

    {
        "status": "success",
        "user": {
            "email": "ayodejioni1505@gmail.com",
            "name": "Oni Ayodeji Mahmuud",
            "stack": "Python/FastAPI"
        },
        "timestamp": "2025-10-16T09:39:52Z",
        "fact": "Florence Nightingale owned more than 60 cats in her lifetime."
    }

Usage

    import requests

    response = requests.get("https://")
    print(response.json())
