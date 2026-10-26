# -*- coding: utf-8 -*-
import requests

from odoo import api, models


class DailyTaxRate(models.Model):
    _name = "daily.tax.rate"
    _description = "Tasa de cambio oficial BCV (dólar y euro)"

    @api.model
    def get_divisas_tasas(self):
        """Consulta la tasa oficial del Dólar y Euro (BCV) desde dolarapi.com"""
        data = {
            "usd": 0.0,
            "eur": 0.0,
            "fecha": "",
        }
        try:
            res_usd = requests.get(
                "https://ve.dolarapi.com/v1/dolares/oficial", timeout=3
            )
            if res_usd.status_code == 200:
                usd_json = res_usd.json()
                data["usd"] = round(float(usd_json.get("promedio", 0.0)), 2)
                data["fecha"] = usd_json.get("fechaActualizacion", "")
        except Exception:
            pass

        try:
            res_eur = requests.get(
                "https://ve.dolarapi.com/v1/euros/oficial", timeout=3
            )
            if res_eur.status_code == 200:
                eur_json = res_eur.json()
                data["eur"] = round(float(eur_json.get("promedio", 0.0)), 2)
        except Exception:
            pass

        return data
