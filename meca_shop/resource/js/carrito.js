document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.item');
    let subtotal = 0;

    items.forEach(item => {
        const priceElement = item.querySelector('.item-price');
        const price = parseFloat(priceElement.textContent.replace('$', ''));
        subtotal += price;
    });

    const iva = subtotal * 0.19;
    const total = subtotal + iva;

    document.querySelector('.subtotal-value').textContent = `$${subtotal.toFixed(2)}`;
    document.querySelector('.iva-value').textContent = `$${iva.toFixed(2)}`;
    document.querySelector('.total-value').textContent = `$${total.toFixed(2)}`;
});
