
// object of all the property of a product in order
class OrderProduct {
    constructor(product, description, price, i) {
        this.product = product
        this.price = price
        this.i = i
        this.description = description
    }

    toText() {
        return `number : ${this.i}\n product : ${this.product} product\n price :  ${this.price}  \n `
    }

}