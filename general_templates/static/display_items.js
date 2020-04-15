function addToCart(itemId, addCartUrl){
    $.ajax({
        url: addCartUrl,
        data: {
            'item_id': itemId
        },
        success: function (response) {
            let alerts = document.getElementById('alerts');
            alerts.innerHTML +=
                `<div class="alert alert-success alert-dismissible" role="alert">
                    Added to cart.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>`
            
        }, 
        error: function (response){
            let notification = '';

            if(response.responseText == 'sold'){
                notification = 'This item has already been sold'
            }else if(response.responseText == 'ownitem')
                notification = 'You cannot purchase your own listing.'
            else if(response.responseText == 'duplicate'){
                notification = 'This item is already in your cart.'
            }else if(response.responseText == 'login'){
                notification = 'You are not logged in.'
            }

            let alerts = document.getElementById('alerts');
            alerts.innerHTML +=
            `<div class="alert alert-danger alert-dismissable" role="alert">
                ${notification}
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>`
        }
    });
}

function test(print){
    window.alert(print);
}