//get a map of product and create and display the product
const ProductMenu = document.querySelector('main')


//create the buttons
for (let keys of Object.keys(main_products)) {
    product = main_products[keys]
    let button = document.createElement('div')
    button.classList.add('product_button', 'Button');
    button.id = product.id + '_me'
    button.title = `Description : ${product.description} \n Price : ${product.price}  $ `

    let price = document.createElement('h1')
    price.textContent = product.price + " ₪"
    let newProduct = document.createElement('img')
    newProduct.src = product.img

    button.appendChild(newProduct)
    button.appendChild(price)
    button.orderProduct = new OrderProduct(product.id, product.description, product.price, null)
    //Add Event Listener to order monitor
    productAddEventListener(button)
    ProductMenu.appendChild(button)

}




