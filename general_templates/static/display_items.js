function addToCart(itemId, addCartUrl, pageType){
    // Get the corresponding quantity input from the html page
    let quantity = $('#item-'+itemId).find('#quantity').val();

    $.ajax({
        method: "GET",
        url: addCartUrl,
        data: {
            'item_id': itemId,
            'quantity': quantity
        },
        success: function (response) {
            let notification = '';
            if(response == 'added'){
                notification = 'Added to cart.';
            }else if(response== 'updated'){
                notification = 'Updated item quantity.';
            }else if(response == 'removed') {
                notification = 'Removed from cart.'
            }else{
                notification = response.responseText;
            }
            
            displayAlert(notification, 'success');
            if(pageType == 'cart'){
                window.location.reload();
            }
            
            updateButtons();

            
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
            }else if(response.responseText == 'noquantity'){
                notification = 'Quantity must be at least 1 to add to cart.'
            }else{
                notification = response.responseText;
            }

            displayAlert(notification, 'danger');
        },
    });
}

function displayAlert(notification, type){
    let alerts = document.getElementById('alerts');
    alerts.innerHTML += 
    `<div class="alert alert-${type} alert-dismissable fade show" role="alert">
        ${notification}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
    </div>`



    // // Set alerts to close after 1 second
    // $('.alert').delay(3000).slideUp(200, function(){
    //     $('.alert').alert('close');
    // });

}

// Update add to cart buttons to reflect the available options depending on the user's cart
function updateButtons(){

    $.ajax({
        type: "GET",
        contentType: "application/json; charset=utf-8",
        url: '/buying/peek_cart',
        // headers: {
        //     'X-CRSFToken': getCSRFToken()
        // },
        data: "data",
        success: function (response) {
            doButtonUpdate(response.cart);
        },
        error: function (response) {
            console.log("error")
        }


    });
}

// Given a list of item ids, update the cart buttons to reflect the users cart
function doButtonUpdate(cart){
    // Reset all button apperance first
     $('.add-cart-button').each(function (cartButton){
        $(this).html('Add to Cart');
        $(this).removeClass('btn-warning');
        $(this).addClass('btn-primary');     
    
    })


    for(var i = 0; i < cart.length; i ++){
        let itemId = cart[i].item_id;
        let cartQuantity = cart[i].quantity;
        let itemCard = $('#item-'+itemId);
        // Set quantity to current cart amount
        if(itemCard){
            itemCard.find('#quantity').val(cartQuantity);
            let cartButton = itemCard.find('#add-cart-button');
            if($('#item-'+itemId).find('#quantity').val() > 0){
                cartButton.html('Update Cart');
                cartButton.removeClass('btn-primary');
                cartButton.addClass('btn-warning');
            }else{
                cartButton.html('Add to Cart');
                cartButton.removeClass('btn-warning');
                cartButton.addClass('btn-primary');

            }
        }
    }
}


// Get crsf token for POST request
function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}


// Update cart buttons on page load
window.onload = function (){
    updateButtons();
}

