import qrcode
from PIL import Image
from PIL import ImageColor

background_color = "#50e19e"
fill_color = "#FFFFFF"

def create_qrcode_with_icon(link, file_name="qrcode.png", icon_path="icone.png", icon_size=0.2):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img_qr = qr.make_image(fill_color=fill_color, back_color=background_color).convert("RGBA")

        qr_size = img_qr.size[0]
        qr_size_px = int(icon_size * qr_size)

        try: 
            img_icon = Image.open(icon_path).convert("RGBA")
            img_icon.thumbnail((qr_size_px, qr_size_px))

            icon_color = ImageColor.getrgb(fill_color)

            icon = Image.new("RGBA", img_icon.size, fill_color)
            icon.paste(img_icon, (0,0), img_icon)

            icon_position = (
                ((qr_size) // 2) - (qr_size_px // 2),
                ((qr_size) // 2) - (qr_size_px // 2),
            )
            img_qr.paste(img_icon, icon_position, img_icon)
        except FileNotFoundError:
            print(f"Aviso: Ícone '{icon_path}' não encontrado. Gerando QR Code sem ícone.")

        img_qr.save(file_name)
        print(f"QR Code gerado com sucesso! Salvo como {file_name}")

    except Exception as e:
        print(f"Erro ao gerar QR Code: {e}")

link = 'https://www.instagram.com/imc.jovem?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='
create_qrcode_with_icon(link, "formulario_qr_code.png", "instagram.png", 0.4)
