import ecommerce_utils
cart={
    "laptop":56000,
    "phone":22000,  
    "headphones":400
    
}
ecommerce_utils.generate_invoice(cart, discount_percent=10, gst_percent=18)