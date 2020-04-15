function addToCart(itemId, addCartUrl){
    // Get the corresponding quantity input from the html page
    let quantity = $('#item-'+itemId).find('#quantity').val();
    $.ajax({
        url: addCartUrl,
        data: {
            'item_id': itemId,
            'quantity': quantity
        },
        success: function (response) {
            let notification = '';
            console.log(response);
            if(response == 'added'){
                notification = 'Added to cart.';
            }else if(response== 'updated'){
                notification = 'Updated quantity.';
            }else{
                notification = response.responseText;
            }
            
            let alerts = document.getElementById('alerts');
            alerts.innerHTML +=
                `<div class="alert alert-success alert-dismissible" role="alert">
                    ${notification}
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>`
            
        }, 
        error: function (response){
            let notification = '';

            if(response.responseText == 'sold'){
                notification = 'This item has already been sold';
            }else if(response.responseText == 'ownitem')
                notification = 'You cannot purchase your own listing.';
            else if(response.responseText == 'duplicate'){
                notification = 'An item of this quantity already exists in your cart. You can either update the quantity or remove it.';
            }else if(response.responseText == 'login'){
                notification = 'You are not logged in.';
            }else{
                notification = response.responseText;
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