YTGrabber - a web app that allows you to download any videos/clips from YouTube for free in different qualities and formats!

## To start using it:
1. Register the account on ngrok(if you haven't yet): [Sign Up Ngrok](https://dashboard.ngrok.com/signup)
2. Create `ngrok.yml` by data from ngrok-example.yml and fill out required data: `authtoken` and `domain`.
3. Create `.env` by data from `.end.dist` and fill out required data.
4. **Run with Docker:**
    1. Download and install `Docker desktop` (if you haven't yet): [Download Docker Desktop](https://docs.docker.com/get-docker/).
    2. Run project with next command in terminal:  
        `docker-compose up --build`
