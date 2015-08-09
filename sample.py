#!/usr/bin/env python3

import python_zxing.zxing as pyzxing

decoder = pyzxing.BarCodeReader("zxing")
print(decoder.decode("sample.png", try_harder=True, qr_only=True).data)