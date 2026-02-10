from fastapi import FastAPI
from fastapi.responses import Response
from mangum import Mangum
from pydantic import BaseModel
from typing import Dict
from datetime import date
from fpdf import FPDF

app = FastAPI()


class InvoiceRequest(BaseModel):
    customer_name: str
    guide_name: str
    date: date
    price: float
    currency: str


def generate_invoice_pdf(invoice: InvoiceRequest) -> bytes:
    pdf = FPDF()
    pdf.add_page()

    FONT_FAMILY = "Helvetica"

    pdf.set_font(FONT_FAMILY, "B", 24)
    pdf.cell(0, 10, "Travel Tours Invoice", ln=True)
    pdf.ln(10)

    pdf.set_font(FONT_FAMILY, "B", 10)
    pdf.cell(15, 6, "Date:")
    pdf.set_font(FONT_FAMILY, "", 10)
    formatted_date = invoice.date.strftime("%B %d, %Y")
    pdf.cell(0, 6, formatted_date, ln=True)

    pdf.set_font(FONT_FAMILY, "B", 10)
    pdf.cell(15, 6, "Name:")
    pdf.set_font(FONT_FAMILY, "", 11)
    pdf.cell(0, 6, invoice.customer_name, ln=True)
    pdf.ln(10)

    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)

    pdf.set_font(FONT_FAMILY, "B", 11)
    pdf.cell(140, 6, "Description", ln=False)
    pdf.cell(0, 6, "Amount", ln=True, align="R")
    pdf.ln(2)

    pdf.set_font(FONT_FAMILY, "", 10)
    pdf.cell(140, 6, f"Guide: {invoice.guide_name}", ln=False)
    pdf.cell(0, 6, f"{invoice.currency} {invoice.price:.2f}", ln=True, align="R")
    pdf.ln(3)

    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(3)

    pdf.set_font(FONT_FAMILY, "B", 11)
    pdf.cell(140, 6, "TOTAL:", ln=False)
    pdf.cell(0, 6, f"{invoice.currency} {invoice.price:.2f}", ln=True, align="R")

    return bytes(pdf.output())


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello from FastAPI on Lambda!"}


@app.post("/generate-invoice")
async def generate_invoice(invoice: InvoiceRequest) -> Response:
    pdf_bytes = generate_invoice_pdf(invoice)
    filename = f"invoice_{invoice.customer_name.replace(' ', '_')}.pdf"

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


lambda_handler = Mangum(app, lifespan="off")
