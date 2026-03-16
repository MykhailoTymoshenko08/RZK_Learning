def email_template(customer):
    return f"""
    Dear {customer['name']},

    Thank you for being a valued customer.
    Your last order was on {customer['last_order_date']}.

    Best regards,
    CRM Team
    """