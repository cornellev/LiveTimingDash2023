# CEV Live Timing Dashboard

Monitoring vehicle metrics.

Make sure the Docker engine is running (Mac and Windows need to download the Docker app). To start, run

```
docker compose up --build
```

This starts the frontend react app, backend, and a Redis server all at the same time on Docker. The specific environments for the frontend and backend is configured in `frontend/Dockerfile` and `backend/Dockerfile`, respectively. Refer to `docker-compose.yml` for more details on what port and what environment variables to pass into these microservices.

### Deployment onto Heroku server

Since Heroku only allows you to deploy one container onto their server (no SSH or anything either), we must consolidate everything into one single container: `Dockerfile.heroku`. Since each Dockerfile only has one command to run at the end, we will use `supervisord.config` to run various commands in the background all at once, with other features like restart, logging and such (better than a bash script).

```
docker build --platform linux/amd64 -f Dockerfile.heroku -t registry.heroku.com/live-timing-dash/web .
docker push registry.heroku.com/live-timing-dash/web
heroku container:release web --app live-timing-dash
```

Build the image with `linux/amd64` to make it compatible with the actual servers running at Heroku. We need to tag each docker container with `registry.heroku.com/live-timing-dash/web` for it to release properly. Then we push it over to the registry what heroku uses for this specific live-timing-dash app. Then we can then use it to release to the linux.

### Debugging tips

Running the container locally to see if the Dockerfile.heroku can be built correctly. However, we recommend using the docker build to enable hot reloads.
```
docker run --rm -p 8000:8000 -p 3000:3000 -p 6379:6379 registry.heroku.com/live-timing-dash/web
```

Checking the error log from the backend if something is not running
```
docker exec -it <docker container id> cat /var/log/backend.err.log
```

To send a test post request to the uc24 endpoint to see if the living timing dash backend is updating the frontend:
```
curl -X POST "http://live-timing-dash.herokuapp.com/api/insert/uc24" \
     -H "Content-Type: application/json" \
     -d '{"accel": 1.5, "gps_lat": 37.7749, "gps_long": -122.4194, "left_rpm": 3000, "right_rpm": 3200, "potent": 75, "temp": 85}'
```