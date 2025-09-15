# SCOUT

Modern full-stack platform scaffold.

## Project Structure

```
SCOUT/
├── frontend/                 # React TypeScript Frontend
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API and Azure service wrappers
│   │   ├── stores/          # Zustand state stores
│   │   ├── hooks/           # Custom React hooks
│   │   ├── types/           # Shared TypeScript types
│   │   ├── utils/           # Utility helpers
│   │   └── config/          # Frontend configuration (env mapping)
│   ├── public/              # Static assets
│   └── package.json         # Frontend dependencies & scripts
├── backend/                  # FastAPI Python Backend
│   ├── app/
│   │   ├── api/             # API route definitions (FastAPI routers)
│   │   ├── core/            # Settings, security, logging, startup
│   │   ├── models/          # Pydantic & ORM models
│   │   ├── services/        # Business/domain services
│   │   ├── ai/              # AI / ML integration modules
│   │   └── websocket/       # WebSocket event handlers
│   ├── alembic/             # Database migrations
│   ├── tests/               # Backend tests
│   └── requirements.txt     # Python dependencies
├── infrastructure/           # Azure oriented infrastructure-as-code
│   ├── terraform/           # Terraform modules & stacks
│   ├── kubernetes/          # Manifests / Helm charts
│   └── docker/              # Dockerfiles & compose
├── docs/                    # Project documentation
└── README.md
```

## Next Steps

- Initialize `frontend` with React + TypeScript tooling (e.g. Vite or Next.js)
- Initialize `backend` FastAPI app structure with config & health endpoint
- Decide on database (e.g. Postgres) and add Alembic env
- Add CI workflow (lint, type-check, test)
- Define infrastructure baseline (Terraform providers, remote state)

## Contributing

1. Create a feature branch
2. Commit with conventional style (e.g. `feat: add user model`)
3. Open a PR and request review

## License

TBD
