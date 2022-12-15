import qrcode


class QrCodeGenerator():
    @staticmethod
    def get_qr(account, price, symbol):
        """Generate image of QR code."""
        message = f"Platba faktury {symbol}"
        img = qrcode.make(
            f"SPD*1.0*ACC:{account}*AM:{price}*CC:CZK*MSG:{message}*X-VS:{symbol}"
            )
        img.save(f"Faktury/QR_Code_{symbol}.png")
