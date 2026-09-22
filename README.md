# Mining Digital Twin Backend

## Project Description
A comprehensive Digital Twin backend for the mining and metallurgical industry. It provides simulation, optimization, diagnostics, and data quality services via a FastAPI application.

## Architecture Overview
- **FastAPI**: Handles API requests and routing.
- **Services**: Business logic layer (simulation, optimization, overview, etc.).
- **Twin**: Core engineering models (mass balance, water balance, kinetic models).
- **Models**: Pydantic models for request/response validation.

## API Endpoints
1. `GET /health` - Service health check
2. `GET /api/v1/plants` - List all plants
3. `GET /api/v1/overview/{plant_id}` - Plant KPIs overview
4. `GET /api/v1/live_state/{plant_id}` - Current live state of the plant
5. `GET /api/v1/timeseries` - Fetch historian timeseries data
6. `GET /api/v1/unit_ops/{plant_id}` - Get unit operations
7. `POST /api/v1/simulate` - Run digital twin simulation
8. `POST /api/v1/optimize` - Run optimization solver
9. `GET /api/v1/control_advisory/{plant_id}` - Get APC control advisories
10. `GET /api/v1/diagnostics/{asset_id}` - Asset diagnostics and anomalies
11. `GET /api/v1/data_quality/{plant_id}` - Tag data quality reports
12. `GET /api/v1/model_metadata/{plant_id}` - Get model version and metadata

## Local Development Setup
1. Clone the repository
2. `python -m venv venv`
3. `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. `pip install -r requirements.txt`
5. `cp .env.example .env`
6. `sh start.sh` or `uvicorn app.main:app --reload`

## Environment Variables
| Variable | Description |
|---|---|
| APP_ENV | Environment (development, production) |
| LOG_LEVEL | Logging level (INFO, DEBUG) |
| ALLOWED_ORIGINS | CORS allowed origins (comma separated) |
| MODEL_VERSION | Digital Twin Model Version |
| DEMO_MODE | Enable demo mode (true/false) |
| PORT | Port for the server |

## Render Deployment Steps
1. Connect GitHub repo to Render.
2. Create a new Web Service.
3. Select the repository and `render.yaml` will auto-configure.
4. Deploy.

## GitHub Setup Steps
1. `git init`
2. `git add .`
3. `git commit -m "Initial commit"`
4. `git branch -M main`
5. `git remote add origin <your-repo-url>`
6. `git push -u origin main`

## Verification Checklist
- [x] All tests pass
- [x] Application starts without errors
- [x] Endpoints return correct JSON structure
- [x] Linting and formatting checked

## Troubleshooting
- **CORS Issues**: Ensure `ALLOWED_ORIGINS` in `.env` includes your frontend URL.
- **Missing Env Vars**: Check `.env` against `.env.example`.
- **Render Build Failures**: Ensure `requirements.txt` is up-to-date.
- **Cold Start**: Render free tier may take up to 50s to wake up.

## API Response Format Examples
```json
{
  "status": "success",
  "timestamp": "2024-01-01T12:00:00Z",
  "data": { ... }
}
```
