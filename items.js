
async function popular(){
    let  response= await fetch('/popular') // pairnoume ta data apo DB
    let popArray=await(response.json())
    let container = document.getElementById('athletes-container').innerHTML; // ftiaxnume container me data
    container.innerHTML=""  // adiazume to container gia na to gemisume swsta 
    for (let i=0;i<5;i++){



    }
}