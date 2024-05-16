from odoo import models, fields, api
from odoo.exceptions import ValidationError
from slugify import slugify


class ProductTemplate(models.Model):
    _inherit = "product.template"

    slug = fields.Char(string="Slug", compute="_compute_slug", store=True)
    additional_barcode = fields.Char(string="Additional Barcode", unique=True)

    @api.depends('name')
    def _compute_slug(self):
        for product in self:
            if product.name:
                product.slug = slugify(product.name)

    @api.constrains("additional_barcode")
    def _check_additional_barcode_unique(self):
        for product in self:
            if product.additional_barcode:
                existing_product = self.env["product.template"].search(
                    [("additional_barcode", "=", product.additional_barcode)]
                )
                if len(existing_product) > 1:
                    raise ValidationError("The additional barcode must be unique.")
