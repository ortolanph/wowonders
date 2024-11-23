import pdfkit
from jinja2 import Template

PDF_OPTIONS = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}
pdfkit_config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
PAGE_TEMPLATE = "template/template.html"


def fill_template(levels):
    with open(PAGE_TEMPLATE, "r") as page_template:
        template = Template(
            page_template.read(),
            trim_blocks=True,
            lstrip_blocks=True)

    rendered_page = template.render(
        levels=levels,
    )

    pdf = pdfkit.from_string(
        rendered_page,
        False,
        options=PDF_OPTIONS,
        configuration=pdfkit_config)

    return pdf
