# CEV Live Timing Dashboard

Monitoring vehicle metrics.

Make sure the Docker engine is running (Mac and Windows need to download the Docker app). To start, run

```
docker compose up --build
```

This starts the frontend react app, backend, and a Redis server all at the same time on Docker. The specific environments for the frontend and backend is configured in `frontend/Dockerfile` and `backend/Dockerfile`, respectively. Refer to `docker-compose.yml` for more details on what port and what environment variables to pass into these microservices.

### Deployment onto Heroku server

Since Heroku only allows you to deploy one container onto their server (no SSH or anything either), we must consolidate everything into one single container: `Dockerfile.heroku`. I am going to use a DinD (Docker inside Docker) approach to orchestrate this. To make sure we have the right permissions running a Docker inside our deployment container, we need to use `supervisord.conf` and some configurations to make sure we have the right system access.

You can check the single container setup for our multi-container docker compose app by running

```
docker build -t my-app .
docker run -p 8000:8000 -p 3000:3000 -p 6379:6379 cev-live-timing
```

You should see the container running after running `docker ps`
