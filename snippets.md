## display product square:
```html
<div class="product">
    <img src="{{ product.img_link }}" alt="{{ product.name }}">
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <p>Quantity: {{ product.product_quantity }}</p>
    <!-- Add more details as needed -->
</div>
```