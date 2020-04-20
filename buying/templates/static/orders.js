function displayOrders(orders, type){
    let orderSection = document.getElementById(type);
    totalPrice = 0;
    console.log(orders);
    if(orders.length == 0){
        orderSection.innerHTML += '<p>There are no orders here yet.</p>';
    }
    for(var i = 0; i < orders.length; i++){
        orderSection.innerHTML += generateOrderHTML(orders[i], type);
    }
}

function generateOrderHTML(order, type){
    // Order details
    let buyer = order.buyer.user.username;
    let quantity = order.quantity;
    let price = order.price;
    let shipping = order.shipping_address;
    let date = order.date;
    let image = order.item.image;
    let item = order.item;


    // Dynamic fields
    let user = ''
    let userTag = ''
    if(type == 'my-purchases'){
        userTag = 'Seller'
        user = order.item.seller.user.username;
    }else{
        userTag = 'Buyer'
        user = order.buyer.user.username;
    }


    html = `
        <li id ="order-${order.order_id}" class="media">
            <a href="#">
                <img src=${image} class="mr-3" width="100" height="100">
            </a>
            <div class="media-body">
                <h5 class="mt-0">${item.name}</h5>
                <p><strong>${userTag}: </strong>${user}</p>
                <p><strong>Amount Paid: </strong>$${price}</p>
                <p><strong>Quantity: </strong>${quantity}</p>
                <p><strong>Date: </strong>${date}</p>

            </div>

        </li>
    `
    return html;
}
