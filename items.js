
async function popular(){
    let  response= await fetch('/popular') // pairnoume ta data apo DB
    let popArray=await(response.json())
    let container = document.getElementById('athletes-container') // ftiaxnume container me data
    container.innerHTML=""  // adiazume to  mesa tou container gia na to gemisume swsta 
    for (let i=0;i<popArray.length;i++){ // gemizw kathe karta name, photo, likes
        let athlete=popArray[i] // athlete exei 1 json item, ara athlete.likes. athlete.photo klp
        container.innerHTML+= generateCard(athlete)
    }
}

async function search(){

    query=document.getElementById('search-input').value
    // sto items, sto searchbar, pernume to value apo oti grapsei mesa sto bar .

  let response=await fetch('/search?name=' +query)
  // psaxnume oti egrapse an yparxei sthn db 

let athletes= await response.json()

  let container = document.getElementById('athletes-container'); // ftiaxnume container me data
    container.innerHTML=""
    // ftiaxnume xwro na boun oi kartes, kai adiazume tocontainer apo palies.

  for (let i=0;i<response.length;i++)
  {
 container.innerHTML+=generateCard(athletes[i])

  }
}




 function generateCard( athlete){ // pairnei 1 item athlete apo to json kai 
    // xrhsimopoiwntas ta athlete.photo, athlete.name etc ftiaxnei thn karta
    // vazw olh thn karta me backticks kai stis metavlites vazw ${athlete.field }
return `<div class="col">
                    <div class="card h-100" id="card-${athlete._id}">
                        <img src="${athlete.photo}" class="card-img-top" alt="${athlete.name}" style="height: 200px; object-fit: cover; object-position: top;">
                        <div class="card-body">
                            <h5 class="card-title">${athlete.name}</h5>
                        </div>
                            <div class="card-footer bg-dark text-warning text-center">
                                <span> 💪 <span class="likes-counter">${athlete.likes} </span> likes </span>
                            </div>
                    </div>
                </div>  `
 }