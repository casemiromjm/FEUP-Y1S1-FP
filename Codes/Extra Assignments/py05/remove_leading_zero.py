def remove_leading(ip):
    digits_together = ip.split(".")

    for i, digits in enumerate(digits_together):
        digits_together[i] = int(digits)

    ip_simplified = f"{digits_together[0]}.{digits_together[1]}.{digits_together[2]}.{digits_together[3]}"

    return ip_simplified