import os
import qrcode


QR_FOLDER = "generated_qr"


os.makedirs(QR_FOLDER, exist_ok=True)


def generate_qr(shop_id: int):

    review_url = (
        f"http://localhost:3000/review/{shop_id}"
    )

    img = qrcode.make(review_url)

    file_path = (
        f"{QR_FOLDER}/shop_{shop_id}.png"
    )

    img.save(file_path)

    return file_path