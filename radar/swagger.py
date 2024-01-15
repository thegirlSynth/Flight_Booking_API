template = {
    "swagger": "2.0",
    "info": {
        "title": "Flight Booking API",
        "description": "API for booking flights",
        "contact": {
            "email": "cynthianuchepro@gmail.com",
            "url": "www.x.com/thegirlSynth",
        },
        "termsOfService": "www.x.com/thegirlSynth",
        "version": "1.0",
    },
    "basePath": "radar",
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer": {"type": "apiKey", "name": "Authorization"},
    },
}


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flassger_static",
    "swagger_ui": True,
    "specs_route": "/",
}
