# Keda Tech Test

### `POST /generate-invoice`

Generates a PDF invoice and returns it as a downloadable file.

**Request Body:**

```json
{
  "customer_name": "John Doe",
  "guide_name": "Jane Smith",
  "date": "2026-02-11",
  "price": 150.00,
  "currency": "USD"
}
```

**Response:**

PDF file download (`application/pdf`)

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Development Server

Run with hot-reload on port 8000:

```bash
docker compose up dev
```

The API will be available at `http://localhost:8000`

### Lambda Emulator

Run the Lambda emulator on port 9000:

```bash
docker compose up lambda
```
