# CEV Live Timing Dashboard

Monitoring vehicle metrics.

Make sure the Docker engine is running (Mac and Windows need to download the Docker app). To start, run

```
docker compose up --build
```

This starts the frontend react app, backend, and a Redis server all at the same time on Docker. The specific environments for the frontend and backend is configured in `frontend/Dockerfile` and `backend/Dockerfile`, respectively.
