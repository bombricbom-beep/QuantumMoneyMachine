from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api.routes import router as lead_router

app = FastAPI(
    title="LeadFlow AI",
    description="AI-powered lead response and qualification SaaS for local service businesses.",
    version="0.1.0",
)

app.include_router(lead_router)


@app.get("/", response_class=HTMLResponse)
async def landing_page() -> str:
    return """
    <html>
      <head>
        <title>LeadFlow AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style>
          body { font-family: Arial, sans-serif; margin: 0; background: #07111f; color: white; }
          .container { max-width: 1100px; margin: 0 auto; padding: 32px 20px 80px; }
          .hero { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 30px; align-items: center; }
          .badge { display: inline-block; padding: 8px 12px; border: 1px solid #2dd4bf; border-radius: 999px; color: #9ae6b4; font-size: 12px; }
          h1 { font-size: 3rem; line-height: 1.1; }
          p { color: #d1d5db; font-size: 1.1rem; }
          .btn { display: inline-block; background: #14b8a6; color: #04141d; padding: 14px 22px; border-radius: 10px; font-weight: bold; text-decoration: none; margin-top: 16px; }
          .card { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 22px; }
          .grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; margin-top: 40px; }
          .price { font-size: 2rem; font-weight: bold; }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="hero">
            <div>
              <div class="badge">AI that replies before your competitors do</div>
              <h1>Turn every lead into a fast, qualified opportunity.</h1>
              <p>LeadFlow AI helps local service businesses answer new leads instantly, qualify them, and route them to the right follow-up flow.</p>
              <a class="btn" href="#pricing">See pricing</a>
            </div>
            <div class="card">
              <h3>How it works</h3>
              <ul>
                <li>Lead comes in from website, WhatsApp, ads or form</li>
                <li>AI qualifies the lead in seconds</li>
                <li>Business gets a priority summary + next action</li>
                <li>Sales follow-up starts immediately</li>
              </ul>
            </div>
          </div>

          <div class="grid" id="pricing">
            <div class="card">
              <h3>Starter</h3>
              <div class="price">$79<span style="font-size: 16px;">/mo</span></div>
              <p>For solo operators and micro-businesses.</p>
            </div>
            <div class="card">
              <h3>Growth</h3>
              <div class="price">$199<span style="font-size: 16px;">/mo</span></div>
              <p>For active service businesses with recurring lead volume.</p>
            </div>
            <div class="card">
              <h3>Scale</h3>
              <div class="price">$499<span style="font-size: 16px;">/mo</span></div>
              <p>For teams managing multiple locations and lead sources.</p>
            </div>
          </div>
        </div>
      </body>
    </html>
    """


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "app": "LeadFlow AI", "version": "0.1.0"}


@app.get("/pricing")
async def pricing() -> dict:
    return {
        "plans": [
            {"name": "Starter", "price": 79, "currency": "USD"},
            {"name": "Growth", "price": 199, "currency": "USD"},
            {"name": "Scale", "price": 499, "currency": "USD"},
        ]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
