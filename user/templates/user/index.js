function renderListingCard(item){
    let listings = document.getElementById('listings');
    let imgUrl = item.img? item.img.url : '#'

    listings.innerHTML += `
    <div class="card mh-25" style="width:18rem; margin:10px;">
        <img class="card-img-top" src"${imgUrl}" width="300px" height="200px">
        <div class="card-body">
            <h5 class="card-title">${item.name}</h5>
            
            <p class="card-text">
            <strong> ${item.seller.user.username} </strong><br>
            {{item.description}}
            </p>


            <button class="btn btn-primary" onclick="">Add to Cart</button>
            <button class="btn" onclick=""> More </button>
        </div>
    </div>

    `
}

function renderAllListings(listings){
    for(var i = 0; i < listings.length; i++){
        console.log(listings[i]);
    }
}