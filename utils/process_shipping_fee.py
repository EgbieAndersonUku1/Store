
def process_shipping_fee(grand_total):
    return (False, grand_total) if grand_total > 100 else (True, round(grand_total + 50, 2))


def _is_shipping_free(grand_total):
        return True if grand_total > 100 else False