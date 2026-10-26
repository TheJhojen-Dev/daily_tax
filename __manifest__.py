# -*- coding: utf-8 -*-
{
    "name": "Daily Tax",
    "version": "18.0.1.0.0",
    "summary": "Tasa oficial BCV de dólar y euro en la barra superior",
    "category": "Extra Apps",
    "author": "Tecnosoft",
    "website": "https://www.tecnosoft.dev",
    "license": "LGPL-3",
    # "web" se necesita porque el módulo inyecta un componente OWL en el systray
    # (bundle de assets del backend: web.assets_backend)
    "depends": [
        "base",
        "web",
    ],
    "data": [
        # El modelo daily.tax.rate necesita ACL para que el cliente lo lea por RPC
        "security/ir.model.access.csv",
    ],
    "assets": {
        "web.assets_backend": [
            "daily_tax/static/src/systray/daily_tax_systray.xml",
            "daily_tax/static/src/systray/daily_tax_systray.js",
        ],
    },
    "installable": True,
    "application": True,
}
