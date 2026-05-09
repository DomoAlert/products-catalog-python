from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Seed sample motor parts products."

    def handle(self, *args, **options):
        products_data = [
            {
                "prodname": "Brake Pad Set",
                "price": Decimal("550.00"),
                "description": "Semi-metallic pads for daily riding and reliable stopping power.",
                "stock": 40,
                "image_url": "https://via.placeholder.com/640x420?text=Brake+Pad+Set",
            },
            {
                "prodname": "Chain and Sprocket Kit",
                "price": Decimal("2150.00"),
                "description": "O-ring chain with front and rear sprockets, 428 pitch.",
                "stock": 18,
                "image_url": "https://via.placeholder.com/640x420?text=Chain+Sprocket+Kit",
            },
            {
                "prodname": "Oil Filter",
                "price": Decimal("180.00"),
                "description": "High-flow oil filter for 150cc to 250cc engines.",
                "stock": 120,
                "image_url": "https://via.placeholder.com/640x420?text=Oil+Filter",
            },
            {
                "prodname": "Air Filter",
                "price": Decimal("260.00"),
                "description": "Washable foam air filter to improve airflow and engine response.",
                "stock": 75,
                "image_url": "https://via.placeholder.com/640x420?text=Air+Filter",
            },
            {
                "prodname": "Spark Plug",
                "price": Decimal("140.00"),
                "description": "Standard heat range plug for smooth idle and clean combustion.",
                "stock": 200,
                "image_url": "https://via.placeholder.com/640x420?text=Spark+Plug",
            },
            {
                "prodname": "Clutch Plate Set",
                "price": Decimal("1850.00"),
                "description": "Friction plate kit for consistent engagement and durability.",
                "stock": 22,
                "image_url": "https://via.placeholder.com/640x420?text=Clutch+Plate+Set",
            },
            {
                "prodname": "LED Headlight Bulb",
                "price": Decimal("950.00"),
                "description": "Bright 6000K LED bulb with low power draw and long life.",
                "stock": 35,
                "image_url": "https://via.placeholder.com/640x420?text=LED+Headlight+Bulb",
            },
            {
                "prodname": "Mirror Set",
                "price": Decimal("320.00"),
                "description": "Universal mirror set with clear view and vibration control.",
                "stock": 60,
                "image_url": "https://via.placeholder.com/640x420?text=Mirror+Set",
            },
        ]

        created = 0
        updated = 0
        for data in products_data:
            product, was_created = Product.objects.update_or_create(
                prodname=data["prodname"],
                defaults={
                    "price": data["price"],
                    "description": data["description"],
                    "stock": data["stock"],
                    "image_url": data["image_url"],
                },
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete. Created: {created}, updated: {updated}."
            )
        )
